import os
import json
from collections import OrderedDict
import pprint



file = os.path.abspath("209-04.json")
f = open(file,'r', encoding="utf-8")
data = json.load(f)


for d in data.values():
    cnt = len(d)
    for k in range(cnt):
        print(d[k]['language'] + " " + d[k]['type'] + " " + d[k]['use'])

