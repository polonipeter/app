from django.shortcuts import render
from .constants import CLIENTID, CLIENTSECERET
from requests import get
from django.http import HttpResponseRedirect

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
