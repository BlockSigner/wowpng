# WOWPNG 📄→🖼

A simple webservice to convert PDFs into high-quality PNGs.

> This is an experiment and not production ready. Use it as inspiration and for learning.

The API is simple, use your favourite tool to interact with it.
Here we demonstrate it with `curl`.

Send the PDF you want to convert:
```
curl -F pdf=@demo.pdf https://wowpng.herokuapp.com/convert
```
In the response you will receive an ID that you can use
to track the progress of the conversion. The ID looks
a bit like `w26ur`. Check the status of the conversion
with the ID `w26ur` by running:
```
curl https://wowpng.herokuapp.com/convert/w26ur
```
Once your conversion is done it will show you
information about the pages it converted with a
JSON response similar to:
```json
{"status": "ok", "id": "w26ur", "job": "ready", "output": {"pages": ["page-0.png", "page-1.png"]}}
```

You can now get your images from:
```
https://wowpng.herokuapp.com/documents/w26ur/page-0.png
https://wowpng.herokuapp.com/documents/w26ur/page-1.png
```

The images will be available for about 10minutes, so you should
retrieve them once they are ready.


## Developing

There are two tasks worth documenting: deploying to heroku and the Python wrapper
for PDFium.


### PDFium bindings

[PyPDFium2](https://github.com/pypdfium2-team/pypdfium2) is used as Python binding
to the PDFium library.


### Heroku

Deploy it your favourite way: auto-deploy via GitHub integration or manually
with a remote like `ssh://git@heroku.com/wowpng.git` called `heroku` and then
running `git push heroku master:master`

You can not use a more modern version of Python in `runtime.txt` until
https://github.com/davidjamesca/ctypesgen/issues/77 is resolved.


### Local development

Install Python 3.7, `pip install -r requirements.txt`, run
`python webserver.py --port=8080`, and `curl` away.


## License

See ``LICENSE`` file in this repository.
