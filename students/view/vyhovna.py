
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from ..models import Vyhovna

#list
def vyhovna(request):
	vyhovna = Vyhovna.objects.all()
	return render(request, 'vyhovna/vyhovna.html', 
		{'vyhovna': vyhovna})

