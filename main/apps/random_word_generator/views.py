# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(req):
    if 'wNumber' not in req.session:
        req.session['wNumber'] = 0
    context = {
        'wNumber': req.session['wNumber'],
        'word': get_random_string(length=14)
    }
    return render(req, 'random_word_generator/index.html', context)

def random_word(req):
    req.session['wNumber'] +=1
    return redirect('/')

def reset(req):
    req.session['wNumber'] = 0
    return redirect('/')