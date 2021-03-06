from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'activities' not in request.session:
        request.session['activities']=[]
    return render(request, "ninja_gold/index.html" )


def gold(request):
    cash = {
    'Metal Detecting Adventure':random.randint(10,20),
    'Back Alley Dice game':random.randint(5,10),
    'Couch Cusion Raid':random.randint(2,5),
    'Casino Card Game':random.randint(-50,50),
    }
    request.session['gold']+=cash[request.POST['building']]
    if cash[request.POST['building']] > 0:
        activity={
            'text': f"you entered a {request.POST['building']} and gained {cash[request.POST['building']]} gold",
            'color': "green"
        }
    else:
        activity= {
            'text': f"you went/entered a {request.POST['building']} and loss {cash[request.POST['building']]} gold",
            'color': "red"
        }

    request.session['activities'].insert(0, activity)
    return redirect('/ninja_gold/')

def reset_gold(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/ninja_gold/')

