from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

import jwt
import json
import datetime

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
		email = request.POST['email']
		password = request.POST['password']
		check_user = User.objects.filter(email = email)
		valid_user = (len(list(check_user)) == 1)
		if (valid_user):
			current_user = email
			request.session['current_user'] = current_user
			#encoded = jwt.encode(payload, secret, algorithm='HS256')
			return render(request, 'login.html', {'msg': 'Login successful'})
		else:
			return render(request, 'login.html', {'msg': 'Failed. Please try again'})
	else:
		return render(request, 'login.html')

@csrf_exempt
def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		print(request.POST)
		existing_email = User.objects.filter(email = email)
		is_new_user = (len(list(existing_email)) == 0)
		print(is_new_user)
		if (is_new_user):
			new_user = User.objects.create(username=username, email=email, password=password)
			new_user.save()
			return render(request, 'signup.html', {'msg': 'Sign up successful'})
		else:
			return render(request, 'signup.html', {'msg': 'Error. Email already exists'})
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
		if request.submit == 'book':
			return render(request, 'book.html')
		else:
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

def book(request):
	if request.method == 'POST':
		objId = request.GET.get('id')
		bookType = request.GET.get('type')
		card_number = request.POST['card_number']
		card_type = request.POST['card_type']
		current_user = request.session['current_user']
		current_date = datetime.datetime.today().strftime('%Y-%m-%d')
		if (bookType == 'flight'):
			travelClass = request.GET.get('class')
			obj = Flight.objects.filter(id = objId).first()
			if (travelClass == 'economy'):
				new_transaction = History.objects.create(userEmail=current_user, bookingType=bookType, bookingStartDate= current_date,paymentAmount=obj.fareEconomy, paymentCardNo=card_number, companyName=obj.companyName, location=obj.destinationLocation)
				new_transaction.save()
			elif (travelClass == 'business'):
				new_transaction = History.objects.create(userEmail=current_user, bookingType=bookType, bookingStartDate= current_date,paymentAmount=obj.fareBusiness, paymentCardNo=card_number, companyName=obj.companyName, location=obj.destinationLocation)
				new_transaction.save()
			elif (travelClass == 'first'):
				new_transaction = History.objects.create(userEmail=current_user, bookingType=bookType, bookingStartDate= current_date,paymentAmount=obj.fareFirst, paymentCardNo=card_number, companyName=obj.companyName, location=obj.destinationLocation)
				new_transaction.save()
		elif (bookType == 'train'):
			travelClass = request.GET.get('class')
			obj = Train.objects.filter(id = objId)
			if (travelClass == 'economy'):
				new_transaction = History.objects.create(userEmail=current_user, bookingType=bookType, bookingStartDate= current_date,paymentAmount=obj.fareEconomy, paymentCardNo=card_number, companyName=obj.companyName, location=obj.destinationLocation)
				new_transaction.save()
			elif (travelClass == 'business'):
				new_transaction = History.objects.create(userEmail=current_user, bookingType=bookType, bookingStartDate= current_date,paymentAmount=obj.fareBusiness, paymentCardNo=card_number, companyName=obj.companyName, location=obj.destinationLocation)
				new_transaction.save()
			elif (travelClass == 'first'):
				new_transaction = History.objects.create(userEmail=current_user, bookingType=bookType, bookingStartDate= current_date,paymentAmount=obj.fareFirst, paymentCardNo=card_number, companyName=obj.companyName, location=obj.destinationLocation)
				new_transaction.save()
		elif (bookType == 'hotel'):
			obj = Hotel.objects.filter(id = objId)
			new_transaction = History.objects.create(userEmail=current_user, bookingType=bookType, bookingStartDate= current_date,paymentAmount=obj.dailyCost, paymentCardNo=card_number, companyName=obj.companyName, location=obj.address)
			new_transaction.save()
		return render(request, 'book.html', {'msg': 'Booking successful'})
	else:
		objId = request.GET.get('id')
		bookType = request.GET.get('type')
		if (bookType == 'flight'):
			travelClass = request.GET.get('class')
			obj = Flight.objects.filter(id = objId)
			return render(request, 'book.html', {'booking':'yes', 'some_list':obj, 'type':bookType, 'class': travelClass})
		elif (bookType == 'train'):
			travelClass = request.GET.get('class')
			obj = Train.objects.filter(id = objId)
			return render(request, 'book.html', {'booking':'yes', 'some_list':obj, 'type':bookType, 'class': travelClass})
		elif (bookType == 'hotel'):
			obj = Hotel.objects.filter(id = objId)
			return render(request, 'book.html', {'booking':'yes', 'some_list':obj, 'type':bookType})
		else:
			return render(request, 'book.html')

def account(request):
	setting = request.GET.get('setting')
	current_user = request.session['current_user']
	if (setting == 'history'):
		history = History.objects.filter(userEmail = current_user)
		return render(request, 'account.html', {'setting': setting, 'transactions': history})
	else:
		return render(request, 'account.html', {'setting': setting})

def logout(request):
	#clear session
	del request.session['current_user']
	return render(request, 'login.html', {'msg': 'Logout successful'})