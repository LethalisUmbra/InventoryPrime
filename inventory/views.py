from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# fomrs and user authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Models
from .forms import UCFCompleted

def home(request):
	login(request)
	return render(request, 'inventory/home.html')

def login(request):
	login_form = AuthenticationForm()
	if request.method == "POST" and 'login_btn':
		login_form = AuthenticationForm(data=request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				do_login(request, user)
				return redirect('home')
	return render(request, 'inventory/login.html')

def register(request):
	login(request)
	register_form = UCFCompleted()

	if request.method == "POST" and 'register_btn':
		register_form = UCFCompleted(request.POST)
		if register_form.is_valid():
			register_form.save();
			return HttpResponseRedirect('/')

	return render(request, 'inventory/register.html', {'register': register_form})