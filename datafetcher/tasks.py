from requests import get

def parse(parse, mode):
    item = parse.get('items')
    name = []
    for i in item:
        name.append(i.get(mode))
    return name

def format_data(data, added):
    out = []
    for i, x in zip(data, added):
        out.append([i,x])
    return out    
    

def get_top(at):
    header = {'Content-Type': 'application/json','Authorization': "Bearer " + at}
    res = get('https://api.spotify.com/v1/me/top/tracks',{},headers=header)
    return res