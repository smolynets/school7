
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from ..models import Podii

#list
def podii(request):
        podii = Podii.objects.all()
	return render(request, 'podii/podii.html', 
		{'podii': podii})



#########################################################################
###adding

def podii_add(request):
  # was form posted?
  if request.method == "POST":
    # was form add button clicked?
    if request.POST.get('add_button') is not None:
      # errors collection
      errors = {}
      # data for student object
      data = {}
      # validate user input
      name = request.POST.get('name', '').strip()
      if not name:
        errors['name'] = u"Заголовок є обов'язковим"
      else:
        data['name'] = name
      text = request.POST.get('text', '').strip()
      if not text:
        errors['text'] = u"Текст є обов'язковим"
      else:
        data['text'] = text
      
      photo = request.FILES.get('photo')
      if photo:
        if photo.name.split(".")[-1].lower() not in ('jpg', 'jpeg', 'png', 'gif'):
           errors['photo'] = u"Файл має бути одного з наступних типів: jpg, jpeg, png, gif"
        else:
           try:
             Image.open(photo)
           except Exception:
             errors['photo'] = u"Завантажений файл не є файлом зображення або пошкоджений"
           else:
             if photo.size > 2 * 1024 * 1024:
                errors['photo'] = u"Фото занадто велике (розмір файлу має бути менше 2Мб)"
             else:
                data['photo'] = photo
           
      # save 
      if not errors:
        podii = Podii(**data)
        podii.save()
        # redirect to podii list
        return HttpResponseRedirect( u'%s?status_message=Подія успішно додана'  % reverse('podii'))
      else:
        # render form with errors and previous user input
        return render(request, 'podii/podii_add_edit.html', {'errors': errors})
    elif request.POST.get('cancel_button') is not None:
      # redirect to home page on cancel button
      return HttpResponseRedirect( u'%s?status_message=Додавання події скасовано!' % reverse('podii'))
  else:
   # initial form render
   return render(request, 'podii/podii_add_edit.html', {})










########################################################################
#####editing

def podii_edit(request, pk):
    events = Podii.objects.filter(pk=pk)

    
    if request.method == "POST":
        data = Podii.objects.get(pk=pk)
        if request.POST.get('edit_button') is not None:
            errors = {}
            
            #fields
            title = request.POST.get('name', '').strip()
            if not title:
                errors['name'] = u"Заголовок є обовʼязковим."
            else:
                data.name = title

            photo = request.FILES.get('photo')
            if photo:
             if len(photo) > (10 * 1024):
               errors['photo'] = u"Файл завеликий"
             else:
               data.photo = photo

            text = request.POST.get('text', '').strip()
            if not text:
                errors['text'] = u"Текст є обовʼязковим."
            else:
                data.text = text

            #errors
            if errors:
                return render(request, 'podii/podii_edit.html', {'pk': pk, 'events': data, 'errors': errors})
            else:
                data.save()
                return HttpResponseRedirect( u'%s?status_message=Подія успішно редагована'  % reverse('podii'))
        elif request.POST.get('cancel_button') is not None:

            return HttpResponseRedirect(u'%s?status_message=Редагування події скасовано!' % reverse('podii'))
        
    else:
        return render(request,
                      'podii/podii_add_edit.html',
                      {'pk': pk, 'podii': events[0]})




#delete podii
def podii_delete(request, pk):
    events = Podii.objects.filter(pk=pk)
    
    if request.method == "POST":
        if request.POST.get('yes') is not None:
          events.delete()
          return HttpResponseRedirect( u'%s?status_message=Подію успішно видалено!'  % reverse('podii'))
        elif request.POST.get('cancel_button') is not None:
          return HttpResponseRedirect( u'%s?status_message=Видалення  події  скасовано!'  % reverse('podii'))
        
    else:
        return render(request,
                      'podii/podii_delete.html',
                      {'pk': pk, 'podii': events[0]})
