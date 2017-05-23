# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'disappearing_ninjas/index.html')

def showAll(request):
    return render(request, 'disappearing_ninjas/ninjas.html')

def showColor(request, color):
    color = color.lower()
    img = {}
    if color in ['blue','orange','red','purple']:
        img['pic'] = 'disappearing_ninjas/images/' + color + '.jpg'
        img['color'] = color
    else:
        img['pic'] = 'disappearing_ninjas/images/notapril.jpg'
        img['color'] = 'notapril'
    return render(request, 'disappearing_ninjas/ninjacolor.html', img)
