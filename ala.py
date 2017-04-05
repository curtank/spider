import pickle
import json
file=open('carddata','rb')
ddata=pickle.load(file)
print(ddata['s'][0])
