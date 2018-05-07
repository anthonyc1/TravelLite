from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

import jwt
import json

from .models import User, Location, Booking, Transportation, Flight, Train, Hotel, Payment, Attraction, Purchase

json_file = open('databaseProj/config_vars.json').read()
data = json.loads(json_file)

@csrf_exempt
def index(request):
	if request.method == 'POST':
		secret = data['secret']
		source = request.POST['source']
		destination = request.POST['destination']
		startdate = request.POST['startdate']
		print(request.POST)
		return render(request, 'index.html',{"results":"ye"})
	else:
		return render(request, 'index.html')
	## figure out how booking will work (send to booking page?)
	

@csrf_exempt
def login(request):
	if request.method == 'POST':
		#print(request.POST.get('email'))
		# if email is in database and checks with password
		if (True):
			payload = {}
			secret = data['secret']
			email = request.POST['email']
			password = request.POST['password']
			encoded = jwt.encode(payload, secret, algorithm='HS256')
			return render(request, 'index.html', {'session': encoded})
		else:
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')

@csrf_exempt
def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		print(request.POST)
		new_user = User.objects.create(username=username, email=email, password=password)
		new_user.save()
		return render(request, 'signup.html')
	else:
		return render(request, 'signup.html')

@csrf_exempt
def hotels(request):
	if request.method == 'POST':
		secret = data['secret']
		location = request.POST['location']
		startdate = request.POST['startdate']
		enddate = request.POST['enddate']
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
		source = request.POST['source']
		destination = request.POST['destination']
		startdate = request.POST['startdate']
		print(request.POST)
		return render(request, 'trains.html',{"results":"ye"})
	else:
		return render(request, 'trains.html')

@csrf_exempt
def explore(request):
	if request.method == 'POST':
		secret = data['secret']
		location = request.POST['location']
		locationArr = location.split(',')
		city = locationArr[0];
		region = locationArr[1];
		#location = Location.objects.filter(city = city).filter(region = region).first()
		location = Location.objects.all()
		location = list(location)
		#attractions = Attraction.objects.select_related(location).all()
		print(location)
		return render(request, 'explore.html',{"results":"yes", "location": location, "some_list":location})
	else:
		return render(request, 'explore.html')

def account(request):
	setting = request.GET.get('setting')
	return render(request, 'account.html', {'setting': setting})

def logout(request):
	#clear session
	#request.session = None
	return render(request, 'index.html')