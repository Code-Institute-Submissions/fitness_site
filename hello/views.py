# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def get_index(request):
    # this is your new view
   return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def home(request):

    return render(request, 'home.html')

