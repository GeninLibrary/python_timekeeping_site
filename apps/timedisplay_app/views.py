# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime
from datetime import datetime

def index(request):
    context = {
        "day":strftime('%b %d, %Y', gmtime()),
        'time': strftime('%-I:%-M %p', gmtime())
    } 
    return render(request,'timedisplay_app/index.html', context)


