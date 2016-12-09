# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Podii
from .models import Biblioteka
from .models import Istoria
from .models import Kolek
from .models import Muzey
from .models import Psuholoh
from .models import Rozklad
from .models import Vyhovna
from .models import Zno


# Create your views here.

def podii(request):
        podii = Podii.objects.all()
	return render(request, 'students/podii.html', 
		{'podii': podii})
###

def biblioteka(request):
        biblioteka = Biblioteka.objects.all()
	return render(request, 'students/biblioteka.html', 
		{'biblioteka': biblioteka})

###
def vyhovna(request):
	vyhovna = Vyhovna.objects.all()
	return render(request, 'students/vyhovna.html', 
		{'vyhovna': vyhovna})

###
def muzey(request):
	muzey = Muzey.objects.all()
	return render(request, 'students/muzey.html', 
		{'muzey': muzey})

###
def kolek(request):
	kolek = Kolek.objects.all()
	return render(request, 'students/kolek.html', 
		{'kolek': kolek})

###
def psuholoh(request):
	psuholoh = Psuholoh.objects.all()
	return render(request, 'students/psuholoh.html', 
		{'psuholoh': psuholoh})

###
def zno(request):
	zno = Zno.objects.all()
	return render(request, 'students/zno.html', 
		{'zno': zno})

###
def rozklad(request):
	rozklad = Rozklad.objects.all()
	return render(request, 'students/rozklad.html', 
		{'rozklad': rozklad})

###
def istoria(request):
	istoria = Istoria.objects.all()
	return render(request, 'students/istoria.html', 
		{'istoria': istoria})


