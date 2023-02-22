import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    # list of defualt chars
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # get what the user chose from html and work with it
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # get the length from html and put the defualt to 12
    length = int(request.GET.get('length', 12))

    password = ''
    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':password})

def about(request):
    return render(request, 'generator/about.html')