# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import random, datetime

def index(request):
    if 'money' not in request.session:
        request.session['money'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = ""
    return render(request, 'ninja_gold/index.html')

def process(request):
    if request.method == 'POST':
        res = ""
        if request.POST['action'] == 'farm':
            val = random.randint(10,20)
            request.session['money'] += val
            res = "Earned {} gold from the farm! ({})\n".format(val, datetime.datetime.now() )
        elif request.POST['action'] == 'cave':
            val = random.randint(5,10)
            request.session['money'] += val
            res = "Earned {} gold from the cave! ({})\n".format(val, datetime.datetime.now() )
        elif request.POST['action'] == 'house':
            val = random.randint(2,5)
            request.session['money'] += val
            res = "Earned {} gold from the house! ({})\n".format(val, datetime.datetime.now() )
        elif request.POST['action'] == 'casino':
            val = random.randint(-50,50)
            request.session['money'] += val
            if val > 0:
                res = "Earned {} gold from the casino! ({})\n".format(val, datetime.datetime.now() )
            elif val < 0:
                res = "Lost {} gold at the casino :( Yikes! ({})\n".format(abs(val), datetime.datetime.now() )
        request.session['activities'] += res
    return redirect(reverse('gold:index'))

def reset(request):
    request.session['money'] = 0
    request.session['activities'] = ""
    return redirect(reverse('gold:index'))
