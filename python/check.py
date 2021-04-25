import json as js

with open("/home/alex/python/1.json","r") as jsf:
    jsv = js.load(jsf)
    print(jsv)