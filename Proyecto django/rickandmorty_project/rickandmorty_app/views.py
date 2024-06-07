import requests
from django.shortcuts import render

def index(request):
    name = request.GET.get('name', '')
    status = request.GET.get('status', '')
    species = request.GET.get('species', '')

    url = 'https://rickandmortyapi.com/api/character'
    params = {
        'name': name,
        'status': status,
        'species': species,
    }

    response = requests.get(url, params=params)
    characters = response.json().get('results', [])

    context = {
        'characters': characters,
        'name': name,
        'status': status,
        'species': species,
    }
    return render(request, 'rickandmorty_app/index.html', context)