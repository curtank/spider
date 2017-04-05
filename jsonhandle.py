import json
s=open("./card.json")
j=json.loads(s.read())
p=[ t for t in j['q']]
for s in p:
    print(s)