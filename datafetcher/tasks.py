from requests import get

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
        for i in range(20):
            artist.append(item[i].get('artists')[0].get('name'))
        return artist

def format_data(first, second, third):
    out = []
    for i, x, z in zip(first, second,third):
        out.append([i,x,z])
    return out     
    

def get_top(at):
    header = {'Content-Type': 'application/json','Authorization': "Bearer " + at}
    res = get('https://api.spotify.com/v1/me/top/tracks',{},headers=header)
    return res