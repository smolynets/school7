
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from ..models import Psuholoh

#list
def psuholoh(request):
	psuholoh = Psuholoh.objects.all()
	return render(request, 'psuholoh/psuholoh.html', 
		{'psuholoh': psuholoh})