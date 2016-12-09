# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Podii(models.Model):
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім’я")
	photo = models.ImageField(
		blank=True,
		null=True,
		verbose_name=u"Фото")

	text = models.TextField(
		blank=False,
		verbose_name=u"текст події")
	def __unicode__(self):
		return u"%s" % (self.name)





class Biblioteka(models.Model):
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім’я")

	text = models.TextField(
		blank=False,
		verbose_name=u"текст події")
	def __unicode__(self):
		return u"%s" % (self.name)





class Istoria(models.Model):
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім’я")

	text = models.TextField(
		blank=False,
		verbose_name=u"текст події")
	def __unicode__(self):
		return u"%s" % (self.name)



	

class Kolek(models.Model):
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім’я")

	text = models.TextField(
		blank=False,
		verbose_name=u"текст події")
	def __unicode__(self):
		return u"%s" % (self.name)




    
class Muzey(models.Model):
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім’я")

	text = models.TextField(
		blank=False,
		verbose_name=u"текст події")
	def __unicode__(self):
		return u"%s" % (self.name)





class Psuholoh(models.Model):
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім’я")

	text = models.TextField(
		blank=False,
		verbose_name=u"текст події")
	def __unicode__(self):
		return u"%s" % (self.name)






class Rozklad(models.Model):
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім’я")

	text = models.TextField(
		blank=False,
		verbose_name=u"текст події")
	def __unicode__(self):
		return u"%s" % (self.name)






class Vyhovna(models.Model):
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім’я")

	text = models.TextField(
		blank=False,
		verbose_name=u"текст події")
	def __unicode__(self):
		return u"%s" % (self.name)


		


class Zno(models.Model):
	name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім’я")

	text = models.TextField(
		blank=False,
		verbose_name=u"текст події")
	def __unicode__(self):
		return u"%s" % (self.name)