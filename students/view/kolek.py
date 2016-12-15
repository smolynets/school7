
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from ..models import Kolek

#list
def kolek(request):
	kolek = Kolek.objects.all()
	return render(request, 'kolek/kolek.html', 
		{'kolek': kolek})
