"""Platzigram views"""

# django
from django.http import HttpResponse
import json

def root(request):
    return redirect('feed')

def hello_world(request):
    """Hello World"""
    return HttpResponse('hello world')

def hi(request):
    """Hi"""
    sorted_numbers = sorted([int(n) for n in request.GET['numbers'].split(',')])

    data = {
        'status': 'ok',
        'data'  : sorted_numbers,
        'msg'   : "Numbers sorted successfully"  
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type="application/json"
        )

def say_hi(request, name, age):
    if age >= 18:
        msg = "Welcome {}".format(name)
    else:
        msg = "Your age is under 18, we sorry {}".format(name)
    
    return HttpResponse(msg)