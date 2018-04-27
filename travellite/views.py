from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

import jwt
import json

json_file = open('databaseProj/config_vars.json').read()
data = json.loads(json_file)

@csrf_exempt
def index(request):
	if request.method == 'POST':
		secret = data['secret']
		print(request.POST)
		return render(request, 'index.html',{"results":"ye"})
	else:
		return render(request, 'trains.html')
	## figure out how booking will work (send to booking page?)
	

@csrf_exempt
def login(request):
	if request.method == 'POST':
		#print(request.POST.get('email'))
		# if email is in database and checks with password
		if (True):
			payload = {}
			secret = data['secret']
			encoded = jwt.encode(payload, secret, algorithm='HS256')
			return render(request, 'index.html', {'session': encoded})
		else:
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')

def signup(request):
	return render(request, 'signup.html')

@csrf_exempt
def hotels(request):
	if request.method == 'POST':
		secret = data['secret']
		#decoded = jwt.verify((request.session.token), data['secret']);
		#valid = jwt.decode(encoded, secret, algorithms=['HS256'])
		print(request.POST)
		#return render(request, 'hotels.html', {'session': session})
		return render(request, 'hotels.html',{"results":"ye"})
	else:
		return render(request, 'hotels.html')
	
@csrf_exempt
def trains(request):
	if request.method == 'POST':
		secret = data['secret']
		print(request.POST)
		return render(request, 'trains.html',{"results":"ye"})
	else:
		return render(request, 'trains.html')

@csrf_exempt
def explore(request):
	if request.method == 'POST':
		secret = data['secret']
		print(request.POST)
		return render(request, 'explore.html',{"results":"ye"})
	else:
		return render(request, 'explore.html')

def account(request):
	setting = request.GET.get('setting')
	return render(request, 'account.html', {'setting': setting})

def logout(request):
	#clear session
	#request.session = None
	return render(request, 'index.html')