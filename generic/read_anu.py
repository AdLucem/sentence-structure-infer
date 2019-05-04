
import requests
import json
import re
from utils.transliterator import translit


def headers(content_len):

    header_dict = {"Host": "sampark.iiit.ac.in",
                   "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0", 
                   "Accept": "application/json, text/javascript, */*; q=0.01",
                   "Accept-Language": "en-US,en;q=0.5",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Referer": "http://sampark.iiit.ac.in/anusaaraka/",
                   "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                   "Content-Length": str(content_len + 29),
                   "Origin": "http://sampark.iiit.ac.in",
                   "Connection": "keep-alive"}

    return header_dict


def translate(sentence):
    """Returns the anusaaraka translated sentence"""

    h = headers(len(sentence))
    url = "https://sampark.iiit.ac.in/Anusaaraka-web-layer-0.4/AnusaarakaService"
    d = {"text": sentence, "srcLang": "eng", "tgtLang": "hin"}

    r = requests.post(url, data=d, headers=h)
    data = json.loads(r.content, encoding="utf-8")
    out = data['output']

    return out
