from django.shortcuts import render
from requests import  post, get
from django.http import HttpResponseRedirect
from .constants import CLIENTID, CLIENTSECERET
from .tasks import get_top, parse, format_data, average, unlock, get_str, sort_a
from .models import user

def authorize_user(request):
    scope = 'user-top-read'
    state = 'a'
    data = {
      'response_type': 'code',
      'client_id': CLIENTID,
      'scope': scope,
      'redirect_uri': 'http://localhost:8000/datafetcher/authorize/get_top',
      'state':state,
    }
    res = get('https://accounts.spotify.com/authorize',params=data)
    redirecturl = res.url
    return HttpResponseRedirect(redirecturl)

def get_access(request):
    author_code =request.GET.get('code')
    data = {
      'grant_type': 'authorization_code',
      'client_id': CLIENTID,
      'client_secret': CLIENTSECERET,
      'redirect_uri': 'http://localhost:8000/datafetcher/authorize/get_top',
      'code': author_code,
    }
    res = post('https://accounts.spotify.com/api/token', data).json()
    access_token = res.get('access_token')
    ret = get_top(access_token)
    data = ret.json()
    ret = parse(data, 'name')
    ret2 = parse(data, 'popularity')
    ret3 = parse(data, 'name', True)
    user.access_token = access_token
    user.name = get_str(ret)  
    user.popularity = get_str(ret2) 
    user.interpret = get_str(ret3) 
    ret = format_data(ret, ret2, ret3)
    return render(request, "index.html", {"data": ret})

def avegare_count(request):
    ret = average(user.popularity)
    name = unlock(user.name)
    popularity = unlock(user.popularity)
    interpret = unlock(user.interpret)
    info = format_data(name, popularity, interpret)
    info[0].append(ret)
    return render(request, "average.html", {"data": info})

def sort_by_alph(request):
    name = unlock(user.name)
    popularity = unlock(user.popularity)
    interpret = unlock(user.interpret)
    info = format_data(name, popularity, interpret)
    info = sort_a(info, 0)
    return render(request, "sort_a.html", {"data": info})

def sort_by_pop(request):
    name = unlock(user.name)
    popularity = unlock(user.popularity)
    interpret = unlock(user.interpret)
    info = format_data(name, popularity, interpret)
    info = sort_a(info, 1)
    return render(request, "sort_p.html", {"data": reversed(info)})

def sort_by_inter(request):
    name = unlock(user.name)
    popularity = unlock(user.popularity)
    interpret = unlock(user.interpret)
    info = format_data(name, popularity, interpret)
    info = sort_a(info, 2)
    return render(request, "sort_i.html", {"data": info})

def basic(request):
    name = unlock(user.name)
    popularity = unlock(user.popularity)
    interpret = unlock(user.interpret)
    info = format_data(name, popularity, interpret)
    return render(request, "index.html", {"data": info})