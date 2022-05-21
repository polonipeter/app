from requests import get
from operator import itemgetter
from django.shortcuts import render

def sort_a(data, index):
    sort = []
    sort = sorted(data, key=itemgetter(index))
    return sort

def average(data):
    data = unlock(data)
    out = 0
    for i in data:
        out += int(i)
    return str(out/(len(data)))

def unlock(data):
    data = data.split("/")
    data.pop(0)
    return data

def get_str(data):
    out = ''
    data = [str(i) for i in data]
    for i in data:
        out+= "/" + i 
    return out

def parse(parse, mode, inlist=None):
    if inlist==None:
        item = parse.get('items')
        name = []
        for i in item:
            name.append(i.get(mode))
        return name
    elif inlist==True:
        item = parse.get('items')
        artist = []
        try:
            for i in range(20):
                artist.append(item[i].get('artists')[0].get('name'))
        except:
            return "not enough data"
        return artist

def make_letter_upper(data):
    data = list(data)
    data[0]=data[0].upper()
    data = "".join(data)
    return data

def format_data(first, second, third):
    out = []
    for i, x, z in zip(first, second, third):
        i = make_letter_upper(i)
        z = make_letter_upper(z)
        out.append([i,int(x),z])
    return out     
    

def get_top(access_token):
    header = {'Content-Type': 'application/json','Authorization': "Bearer " + access_token}
    res = get('https://api.spotify.com/v1/me/top/tracks',{},headers=header)
    return res