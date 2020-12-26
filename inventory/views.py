from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Formulario y Autenticación del Usuario
from django.contrib.auth import login as do_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

def home(request):
	login(request)
	return render(request, 'inventory/home.html')

def login(request):

	# codigo para el formulario del login con autenticación
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