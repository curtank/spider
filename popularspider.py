import requests
import json
r=requests.get("https://hsreplay.net/analytics/query/card_played_popularity_report?GameType=RANKED_STANDARD&RankRange=ALL&TimeRange=LAST_14_DAYS")
#f=open('card.html','w')
#f.write(r.content.decode())
li=r.text
li="{\"s\":"+li+"}"
ddata=json.loads(li)
f=open('populardata','wb')
import pickle
pickle.dump(ddata,f)
