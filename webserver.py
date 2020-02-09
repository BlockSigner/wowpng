import datetime
import json
import logging
import os
import random
import string
import subprocess
import time

from concurrent.futures import ThreadPoolExecutor
from tempfile import TemporaryDirectory

import tornado
from tornado import log
from tornado import options
from tornado import web


options.define("port", default=5000, help="Listen on this port", type=int)


def pdf_to_png(fname, **kwargs):
    p = subprocess.run(["python", "pdf-to-png.py", fname], capture_output=True)
    '''p = subprocess.run(
        [
            "python",
            "-c",
            """
import time
tick = time.time()
while time.time() - tick < 50:
  x = 4 / 5.
print(tick, time.time())
         """,
        ],
        capture_output=True,
    )'''
    return {
        "returncode": p.returncode,
        "stdout": p.stdout.decode("utf-8"),
        "stderr": p.stderr.decode("utf-8"),
    }


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)


json._default_encoder = JSONEncoder()


class BaseHandler(web.RequestHandler):
    @property
    def pdfs(self):
        return self.settings["pdfs"]

    @property
    def jobs(self):
        return self.settings["jobs"]

    @property
    def work_dir(self):
        return self.settings["work_dir"]


class ConversionHandler(BaseHandler):
    def job_id(self):
        return "".join(
            [random.choice(string.ascii_lowercase + string.digits) for _ in range(5)]
        )

    async def post(self):
        """Submit a new conversion job"""
        job = self.job_id()

        self.write({"status": "ok", "id": job})

        pdf = self.request.files["pdf"][0]
        log.app_log.info("uploaded file %s %s", pdf["filename"], pdf["content_type"])

        job_dir = os.path.join(self.work_dir, job)
        fname = os.path.join(job_dir, "document.pdf")

        os.makedirs(job_dir)
        with open(fname, "wb") as f:
            f.write(pdf["body"])

        result = self.settings["pool"].submit(pdf_to_png, fname)
        self.jobs[job] = {"start": time.time(), "task": result}

    async def get(self, job_id):
        """Get the status of a conversion job"""
        if job_id in self.jobs and self.jobs[job_id]["task"].done():
            result = self.jobs[job_id]["task"]
            output = result.result()

            # something went wrong, send stdout and stderr
            if output["returncode"]:
                self.write(
                    {"status": "ok", "id": job_id, "job": "failed", "output": output}
                )

            else:
                self.write(
                    {
                        "status": "ok",
                        "id": job_id,
                        "job": "ready",
                        "output": json.loads(output["stdout"]),
                    }
                )

        else:
            self.write({"status": "ok", "id": job_id, "job": "busy"})


class PingHandler(BaseHandler):
    async def get(self):
        self.finish("pong")


class DatetimeHandler(BaseHandler):
    async def get(self):
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"now": datetime.datetime.utcnow()}) + "\n")


class Application(web.Application):
    def __init__(self):

        work_dir = TemporaryDirectory()
        log.app_log.info("Using '%s' as working direcctory.", work_dir.name)

        handlers = [
            (r"/", PingHandler),
            (r"/convert/([^/]+)", ConversionHandler),
            (r"/convert/?", ConversionHandler),
            (r"/datetime", DatetimeHandler),
            (r"/documents/(.*)", web.StaticFileHandler, {"path": work_dir.name}),
        ]

        pool = ThreadPoolExecutor(2)

        settings = dict(pdfs={}, jobs={}, pool=pool, work_dir=work_dir.name)
        super(Application, self).__init__(handlers, **settings)


async def main():
    # all the logging output
    for logger in (log.app_log, log.access_log, log.gen_log):
        channel = logging.StreamHandler()
        channel.setFormatter(log.LogFormatter())
        logger.addHandler(channel)
        logger.propagate = False
        logger.setLevel(logging.INFO)

    app = Application()
    app.listen(options.options.port, xheaders=True)


if __name__ == "__main__":
    options.parse_command_line()

    io_loop = tornado.ioloop.IOLoop.current()
    io_loop.spawn_callback(main)
    io_loop.start()
