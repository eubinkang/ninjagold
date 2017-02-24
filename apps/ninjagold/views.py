from django.shortcuts import render, redirect
from random import random, randint
from datetime import datetime


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'log' not in request.session:
        request.session['log'] = ""

    return render(request, 'ninjagold/index.html')

def process(request):
    if request.method == 'POST':
        if request.POST.get("building") == 'farm':
            rn = randint(10,15)
            request.session['gold'] = request.session['gold'] + rn
            farmvar = request.session['log'] + "You went to the Farm and got {} gold".format(rn) +" "+ str(datetime.now())
            request.session['log'] = farmvar + "\n"

        elif request.POST.get("building") == 'cave':
            rn = randint(5,20)
            request.session['gold'] = request.session['gold'] + rn
            cavevar = request.session['log'] + "You went to the Cave and got {} gold".format(rn) +" "+ str(datetime.now())
            request.session['log'] = cavevar + "\n"

        elif request.POST.get("building") == 'town':
            rn = randint(0,25)
            request.session['gold'] = request.session['gold'] + rn
            townvar = request.session['log'] + "You went to the Town and got {} gold".format(rn) +" "+ str(datetime.now())
            request.session['log'] = townvar + "\n"

        elif request.POST.get("building") == 'casino':
            rn = randint(-50,50)
            request.session['gold'] = request.session['gold'] + rn
            if rn >= 0:
                casinovar = request.session['log'] + "You went to the Casino and got {} gold".format(rn) +" "+ str(datetime.now())
                request.session['log'] = casinovar + "\n"
            else:
                casinovar = request.session['log'] + "You went to the Casino and lost {} gold".format(rn) +" "+ str(datetime.now())
                request.session['log'] = casinovar + "\n"

    return redirect('/')
