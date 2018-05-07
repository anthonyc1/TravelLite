from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

import jwt
import json

from .models import User, Location, History, Flight, Train, Hotel, Payment, Attraction

json_file = open('databaseProj/config_vars.json').read()
data = json.loads(json_file)

@csrf_exempt
def index(request):
	if request.method == 'POST':
		secret = data['secret']
		source = request.POST['source']
		sourceArr = source.split(',')
		sourceCity = sourceArr[0];
		destination = request.POST['destination']
		destinationArr = destination.split(',')
		destinationCity = destinationArr[0];
		startdate = request.POST['startdate']
		flightClass = request.POST['class']
		flights = Flight.objects.filter(sourceLocation = sourceCity).filter(destinationLocation=destinationCity)
		flights = list(flights)
		print(request.POST)
		return render(request, 'index.html',{"results":"yes", "some_list": flights, "class":flightClass})
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
		locationArr = location.split(',')
		locationCity = locationArr[0];
		startdate = request.POST['startdate']
		enddate = request.POST['enddate']
		hotels = Hotel.objects.filter(city = locationCity)
		hotels = list(hotels)
		#decoded = jwt.verify((request.session.token), data['secret']);
		#valid = jwt.decode(encoded, secret, algorithms=['HS256'])
		print(request.POST)
		#return render(request, 'hotels.html', {'session': session})
		return render(request, 'hotels.html',{"results":"yes", "some_list": hotels})
	else:
		return render(request, 'hotels.html')
	
@csrf_exempt
def trains(request):
	if request.method == 'POST':
		secret = data['secret']
		source = request.POST['source']
		sourceArr = source.split(',')
		sourceCity = sourceArr[0];
		destination = request.POST['destination']
		destinationArr = destination.split(',')
		destinationCity = destinationArr[0];
		startdate = request.POST['startdate']
		trainClass = request.POST['class']
		trains = Train.objects.filter(sourceLocation = sourceCity).filter(destinationLocation=destinationCity)
		trains = list(trains)
		print(request.POST)
		return render(request, 'trains.html',{"results":"yes", "some_list": trains, "class":trainClass})
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
		location = Location.objects.filter(city = city)
		attraction = Attraction.objects.filter(city = city)
		location = list(location)
		return render(request, 'explore.html',{"results":"yes", "location": location, "some_list":attraction})
	else:
		return render(request, 'explore.html')

def account(request):
	setting = request.GET.get('setting')
	return render(request, 'account.html', {'setting': setting})

def logout(request):
	#clear session
	#request.session = None
	return render(request, 'index.html')