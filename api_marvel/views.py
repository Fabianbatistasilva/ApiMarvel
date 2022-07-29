from multiprocessing import context
from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    marvel=requests.get('https://gateway.marvel.com/v1/public/comics?ts=1&apikey=998d4fbbf454824314ac967bb64d0158&hash=9c95b9717bfea2eaa49400e14535256c').json()
    marvel=marvel['data']['results']
    context={'marvel':marvel}
    return render(request,'paginas/home.html',context)