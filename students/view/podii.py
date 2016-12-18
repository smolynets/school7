
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views.generic import CreateView,UpdateView, ListView, DeleteView
from ..models import Podii
from crispy_form import form
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Button

#list
class Podii_List(ListView):
  model = Podii
  context_object_name = 'podii'
  template_name = 'podii/podii.html'
  def get_queryset(self):
    qs = super(Podii_List, self).get_queryset()
    return qs



        

#########################################################################
###adding
#crispy

class PodiiCreateForm(form):
    

    def __init__(self,*args, **kwargs):
        super(PodiiCreateForm,self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('podii_add')
        
        self.helper.layout.fields.append(FormActions(
            Submit('add_button', (u'Створити'), css_class="btn btn-primary"),
            Submit('cancel_button', (u'Скасувати'), css_class="btn btn-link"),
)) 

class PodiiCreate(CreateView):
  model = Podii
  template_name = 'podii/podii_add_edit.html'
  form_class = PodiiCreateForm
  def get_success_url(self):
    return u'%s?status_message=Подію успішно створено!' % reverse('podii')
  def post(self, request, *args, **kwargs):
    if request.POST.get('cancel_button'):
      return HttpResponseRedirect(u'%s?status_message=Створення події відмінено!'% reverse('podii'))
    else:
      return super(PodiiCreate, self).post(request, *args, **kwargs)











########################################################################
#####editing

#crispy
class PodiiUpdateForm(form):
  
  def __init__(self, *args, **kwargs):
      super(PodiiUpdateForm, self).__init__(*args, **kwargs)
      
      
      self.helper.layout.fields.append(FormActions(
        Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
        Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
      ))



class PodiiUpdate(UpdateView):
  model = Podii
  template_name = 'podii/podii_add_edit.html'
  form_class = PodiiUpdateForm
  def get_success_url(self):
    return u'%s?status_message=Подію успішно збережено!' % reverse('podii')
  def post(self, request, *args, **kwargs):
    if request.POST.get('cancel_button'):
      return HttpResponseRedirect(u'%s?status_message=Редагування події відмінено!'% reverse('podii'))
    else:
      return super(PodiiUpdate, self).post(request, *args, **kwargs)








#######################################################################
#delete podii
#stud_delete
class PodiiDelete(DeleteView):
  model = Podii
  template_name = 'podii/podii_delete.html'
  def get_success_url(self):
    return u'%s?status_message=Подію успішно видалено!' % reverse('podii')
  def post(self, request, *args, **kwargs):
    if request.POST.get('no_delete_button'):
      return HttpResponseRedirect(u'%s?status_message=Видалення  події відмінено!'% reverse('podii'))
    else:
      return super(PodiiDelete, self).post(request, *args, **kwargs)

