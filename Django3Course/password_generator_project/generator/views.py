from django.shortcuts import render
from django.http import HttpResponse
import random
from django.db.models.functions import Upper

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):

        characters = list('abcdefghijklmnopqrstuvwsyz')
        upperCharcters = [x.upper() for x in characters]

        if request.GET.get('uppercase'):
            characters.extend(upperCharcters)

        if request.GET.get('special'):
            characters.extend(list('!@£$%^&*'))

        if request.GET.get('numbers') :
            characters.extend(list('1234567890'))

        lenhth = int(request.GET.get('lenhth', 12))
        #thepassword =  ''
        #for x in range(lenhth):
            #thepassword += random.choice(characters)
        thepassword = ''.join(map(str, [random.choice(characters) for x in range(lenhth)]))
        return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
