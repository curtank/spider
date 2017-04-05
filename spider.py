import requests
import json
r=requests.get("https://api.hearthstonejson.com/v1/latest/enUS/cards.json")
#f=open('card.html','w')
#f.write(r.content.decode())
li=r.text
li="{\"s\":"+li+"}"
ddata=json.loads(li)
f=open('carddata','wb')
import pickle
pickle.dump(ddata,f)
