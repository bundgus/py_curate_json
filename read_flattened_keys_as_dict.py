import json

filename = r'output/businessRecord-flattened_keys.json'
with open(filename, 'r') as f:
    rawjson = f.read()
    djson = json.loads(rawjson)

pk = djson.keys()
pkl = list(pk)
pkl.sort()

for i in pkl:
    print(i)
