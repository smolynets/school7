
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from ..models import Muzey

#list
def muzey(request):
	muzey = Muzey.objects.all()
	return render(request, 'muzey/muzey.html', 
		{'muzey': muzey})