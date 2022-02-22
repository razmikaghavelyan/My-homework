import json
import os
from django.shortcuts import HttpResponse
from datetime import datetime


def home(request):
    return HttpResponse("<h1>Welcome to my first website</h1>")


def daytime(request):
    time = str(datetime.utcnow())
    return HttpResponse(time)


def introduction(request):
    return HttpResponse("This site can give you a daytime right now, if you write on browser /daytime")


def square_keys(request):
    return HttpResponse("dict_1 = {} <br> for i in range(1, 15): <br> dict_1[i] = i**2")



