from django.shortcuts import render

import requests
import json

# Create your views here.
def index(request):
    #first api lunar 
    import requests

    key = "uiih24li2wtgm0e1bpc1i"
    symbol = "BTC"
    url = "https://api.lunarcrush.com/v2?data=assets&key="+key+"&symbol="+symbol

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()

    """
    url = "https://api.lunarcrush.com/v2"
    
    payload={}
    headers = {
        'data' :'assets',
        'key' : 'uiih24li2wtgm0e1bpc1i',
        'symbol' : 'BTC'

    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    """
    #print(res)
    context = {
        "obj": res
    }
    return render(request,'index.html',context)