
import requests
import json

def translit(word):

    d = {"eID": "sgAjax",
            "extensionName": "SgTransliterator",
            "controller": "Ajax\Transliterator",
            "action": "translate",
            "format": "json",
            "parameters[text]": word,
            "parameters[from]": "slp1",
            "parameters[to]": "devanagari"}
    url = "https://www.ashtangayoga.info/index.php"
    r = requests.post(url, data=d)
    out = json.loads(r.content, encoding="utf-8")
    out = out['translation']
    out = out.rstrip("<br />\n")
    return out
