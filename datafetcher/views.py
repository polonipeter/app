from django.shortcuts import render
from requests import  post, get
from django.http import HttpResponseRedirect
from .constants import CLIENTID, CLIENTSECERET
from .tasks import get_top, parse, format_data

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
    user = get('https://accounts.spotify.com/authorize',params=data)
    redirecturl = user.url
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
    ret = format_data(ret, ret2)
    return render(request, "index.html", {"name": ret})