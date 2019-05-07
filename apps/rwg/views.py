from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
    "unique_id" : get_random_string(length=14)
    if request.session['counter'] >0
        request.session['counter'] = 1
    else:
        request.session['counter'] +=
    }
    return render(request,'rwg/index.html', context)

def reset(request):
    del request.session['counter']
    return redirect('/')
