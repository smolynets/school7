
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from ..models import Zno

#list
def zno(request):
	zno = Zno.objects.all()
	return render(request, 'zno/zno.html', 
		{'zno': zno})