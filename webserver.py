import datetime
import json
import logging
import random
import string
import subprocess

from concurrent.futures import ThreadPoolExecutor

import tornado
from tornado import log
from tornado import options
from tornado import web


options.define("port", default=5000, help="Listen on this port", type=int)


def doit(fname, **kwargs):
    #p = subprocess.run(
    #    ["python", "pdf-to-png.py", fname], capture_output=True
    #)
    p = subprocess.run(
        ["python", "-c",
         '''
         """
         import time
         tick = time.time()
         while time.time() - tick < 50:
             x = 4 / 5.
         print(tick, time.time())
         """
         '''], capture_output=True
    )
    return p.stdout.decode("utf-8")


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


class DoIt(BaseHandler):
    def job_id(self):
        return "".join(
            [
                random.choice(string.ascii_lowercase + string.digits)
                for _ in range(5)
            ]
        )

    async def post(self):
        """Submit a new 'do it' job"""
        job = self.job_id()

        self.write({"status": "ok", "id": job})

        result = self.settings["pool"].submit(doit, 2)
        self.jobs[job] = result

    async def get(self, job_id):
        """Status of a 'do it' job"""
        if job_id in self.jobs:
            result = self.jobs[job_id]
            if result.done():
                output = result.result()
                self.write(
                    {
                        "status": "ok",
                        "id": job_id,
                        "job": "ready",
                        "output": output,
                    }
                )
                return

        self.write({"status": "ok", "id": job_id, "job": "busy"})


class PingHandler(BaseHandler):
    async def get(self):
        self.finish("pong")


class DatetimeHandler(BaseHandler):
    async def get(self):
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"now": datetime.datetime.utcnow()}) + "\n")


class Application(web.Application):
    def __init__(self,):

        handlers = [
            (r"/", PingHandler),
            (r"/doit/([^/]+)", DoIt),
            (r"/doit/?", DoIt),
            (r"/datetime", DatetimeHandler),
        ]

        pool = ThreadPoolExecutor(2)

        settings = dict(pdfs={}, jobs={}, pool=pool)
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
