from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def signup(request):
	return render(request, 'signup.html')

def hotels(request):
	return render(request, 'hotels.html')

def trains(request):
	return render(request, 'trains.html')

def explore(request):
	return render(request, 'explore.html')

def account(request):
	setting = request.GET.get('setting')
	return render(request, 'account.html', {'setting': setting})