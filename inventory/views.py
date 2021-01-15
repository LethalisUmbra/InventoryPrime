from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

# fomrs and user authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Models
from .forms import UCFCompleted
from primary.models import *

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
		else:
			messages.error(request, 'Username and password do not match.')
			return render(request, 'inventory/login.html')
	return render(request, 'inventory/login.html')

def register(request):
	login(request)
	register_form = UCFCompleted()

	if request.method == "POST" and 'register_btn':
		register_form = UCFCompleted(request.POST)
		if register_form.is_valid():
			user = register_form.save();
			user = authenticate(username=register_form.cleaned_data['username'],
                                password=register_form.cleaned_data['password1'],
                                )
			do_login(request, user)

			# Bow Weapons
			cernos = Bow(name_bow="Cernos Prime", owner=user)
			cernos.save()
			paris = Bow(name_bow="Paris Prime", owner=user)
			paris.save()
			# Rifle Weaopns
			baza = Rifle(name_rifle="Baza Prime", owner=user)
			baza.save()
			boltor = Rifle(name_rifle="Boltor Prime", owner=user)
			boltor.save()
			braton = Rifle(name_rifle="Braton Prime", owner=user)
			braton.save()
			burston = Rifle(name_rifle="Burston Prime", owner=user)
			burston.save()
			latron = Rifle(name_rifle="Latron Prime", owner=user)
			latron.save()
			panthera = Rifle(name_rifle="Panthera Prime", owner=user)
			panthera.save()
			soma = Rifle(name_rifle="Soma Prime", owner=user)
			soma.save()
			stradavar = Rifle(name_rifle="Stradavar Prime", owner=user)
			stradavar.save()
			sybaris = Rifle(name_rifle="Sybaris Prime", owner=user)
			sybaris.save()
			tiberon = Rifle(name_rifle="Tiberon Prime", owner=user)
			tiberon.save()

			# Shotgun Weapons
			tigris = Shotgun(name_shotgun="Tigris Prime", owner=user)
			tigris.save()
			corinth = Shotgun(name_shotgun="Corinth Prime", owner=user)
			corinth.save()
			boar = Shotgun(name_shotgun="Boar Prime", owner=user)
			boar.save()

			# Sniper Weapons
			vectis = Sniper(name_sniper="Vectis Prime", owner=user)
			vectis.save()
			rubico = Sniper(name_sniper="Rubico Prime", owner=user)
			rubico.save()

			# Zhuge Weapons
			zhuge = Zhuge(name_zhuge="Zhuge Prime", owner=user)
			zhuge.save()

			return HttpResponseRedirect('/')
		else:
			messages.error(request, 'Username is not available.')
			return render(request, 'inventory/register.html', {'register': register_form})

	return render(request, 'inventory/register.html', {'register': register_form})