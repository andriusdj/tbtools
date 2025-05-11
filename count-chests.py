#!/bin/python3

import sys
import json

records = json.load(open(sys.argv[1]))
values = json.load(open(sys.argv[2]))

result = {}
for name in records:
    if name not in result:
        result[name] = 0
    for chest in values:
        if chest in records[name]:
            result[name] = result[name] + records[name][chest] * values[chest]

for name in result:
    print(name, "\t",result[name])


