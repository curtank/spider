import pickle
import json
def findnamebydbfid(id,cardset):
    for card in cardset:
        #print(card)
        try:
            card['dbfId']
        except Exception:
            continue
            pass
        if card['dbfId']==id:
            return card['name']
    return 'not find'

file=open('populardata','rb')
ddata=pickle.load(file)
majority=[]
#print(ddata['s']['series']['data']['ALL'][0])
for j in ddata['s']['series']['data']['ALL']:
    if float(j['popularity'])>0.05:
        majority.append(j)
print(majority)
file=open('carddata','rb')
carddata=pickle.load(file)
#print(carddata['s'])
def cmpbypo(x,y):
    return cmp(float(x['popularity']),float(y['popularity']))
majority=sorted(majority,key=lambda card:float(card['popularity']))
for p in majority:
    name=findnamebydbfid(p['dbf_id'],carddata['s'])
    print(name+"  "+p['popularity'])

print(len(majority))