
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views.generic import CreateView,UpdateView, ListView, DeleteView
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Button
from ..models import Podii

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

class PodiiCreateForm(ModelForm):
    class Meta:
        model = Podii
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(PodiiCreateForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

            # return HttpResponseRedirect(
            #     u'%s?status_message=5' %  reverse('main'))


        # set form tag attributes
        self.helper.form_action = reverse('podii_add')
        # self.helper.form_action = u'%s?status_message=5' % reverse('podii_add')

        self.helper.form_method = 'POST'
        self.helper.form_class = 'col-sm-12 form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-8 input-group'

        # add buttons
        # self.helper.layout.fields.append(self)
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
class PodiiUpdateForm(ModelForm):
  class Meta:
    model = Podii
  def __init__(self, *args, **kwargs):
      super(PodiiUpdateForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper(self)
      # set form tag attributes
      self.helper.form_action = reverse('podii_edit',kwargs={'pk': kwargs['instance'].id})
      self.helper.form_method = 'POST'
      self.helper.form_class = 'form-horizontal'
      # set form field properties
      self.helper.help_text_inline = True
      self.helper.html5_required = True
      self.helper.label_class = 'col-sm-2 control-label'
      self.helper.field_class = 'col-sm-10'
      # add buttons
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

