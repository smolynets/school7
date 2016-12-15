
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from ..models import Istoria

#list
def istoria(request):
	istoria = Istoria.objects.all()
	return render(request, 'istoria/istoria.html', 
		{'istoria': istoria})