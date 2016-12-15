
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from ..models import Rozklad

#list
def rozklad(request):
	rozklad = Rozklad.objects.all()
	return render(request, 'rozklad/rozklad.html', 
		{'rozklad': rozklad})
		