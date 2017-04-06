
import requests
import json
r=requests.get("https://hsreplay.net/analytics/query/list_decks_by_win_rate?GameType=RANKED_STANDARD&RankRange=ALL&TimeRange=LAST_30_DAYS")
#f=open('card.html','w')
#f.write(r.content.decode())
li=r.text
li="{\"s\":"+li+"}"
ddata=json.loads(li)
f=open('deckpo','wb')
import pickle
pickle.dump(ddata,f)
