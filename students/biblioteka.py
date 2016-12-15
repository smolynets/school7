# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from ..models import Biblioteka


#list
def biblioteka(request):
        biblioteka = Biblioteka.objects.all()
	return render(request, 'students/biblioteka.html', 
		{'biblioteka': biblioteka})