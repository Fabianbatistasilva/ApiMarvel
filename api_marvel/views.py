from multiprocessing import context
from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    marvel=requests.get('https://gateway.marvel.com/v1/public/series?ts=1&apikey=998d4fbbf454824314ac967bb64d0158&hash=9c95b9717bfea2eaa49400e14535256c').json()
    marvel=marvel['data']['results']
    print(marvel)
    context={'marvel':marvel}
    return render(request,'paginas/home.html',context)
def comics(request):
    marvel=requests.get('https://gateway.marvel.com/v1/public/comics?ts=1&apikey=998d4fbbf454824314ac967bb64d0158&hash=9c95b9717bfea2eaa49400e14535256c').json()
    marvel=marvel['data']['results']
    context={'marvel':marvel}
    return render(request,'paginas/comics.html',context)
def comicsEspec(request,id):
    marvel=requests.get(f'https://gateway.marvel.com:443/v1/public/comics/{id}?ts=1&apikey=998d4fbbf454824314ac967bb64d0158&hash=9c95b9717bfea2eaa49400e14535256c').json()
    marvel=marvel['data']['results']
    print(marvel)
    context={'marvel':marvel}
    return render(request,'paginas/comicsEspecifico.html',context)