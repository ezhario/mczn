# ~*~ coding: utf-8 ~*~

from django.db import models
from django.contrib import admin

import datetime
from django.utils import timezone

# Create your models here.

GENDER = (('none', 'Не определен'), ('male', 'Мужчина'), ('female', 'Женщина'))
CITY = (('perm', 'Пермь'), ('krasnokamsk', 'Краснокамск'), ('berez', 'Березники'), ('dobr', 'Добрянка'), ('pol', 'Полазна'))
DISTRICT = (('dz', 'Дзержинский'), ('in', 'Индустриальный'), ('ki', 'Кировский'), ('le', 'Ленинский'), ('mo', 'Мотовилихинский'), ('or', 'Орджоникидзевский'), ('sv', 'Свердловский'))

class User(models.Model):
	username = models.CharField(unique=True, max_length=100)
	phone = models.CharField(unique=True, max_length=10)
	surname = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	patronymic = models.CharField(max_length=100)
	date_of_birth  = models.DateField()
	gender = models.CharField(choices=GENDER, max_length=10, default='none')
	city = models.CharField(choices=CITY, max_length=20, default='perm')
	district = models.CharField(max_length=20, choices=DISTRICT)
	street = models.CharField(max_length=20)
	building = models.CharField(max_length=20)
	room = models.IntegerField(max_length=4)
	invited_by = models.ForeignKey('self')
	invite_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	password =  models.CharField(max_length=128)
	penalty = models.IntegerField()
	def __unicode__(self):
        	return self.username