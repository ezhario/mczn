# ~*~ coding: utf-8 ~*~

from django.db import models
from django.contrib import admin

import datetime
from django.utils import timezone

from django.forms import ModelForm

# Create your models here.

GENDER = (('none', 'Не определен'), ('male', 'Мужчина'), ('female', 'Женщина'))
CITY = (('perm', 'Пермь'), ('krasnokamsk', 'Краснокамск'), ('berez', 'Березники'), ('dobr', 'Добрянка'), ('pol', 'Полазна'))
DISTRICT = (('dz', 'Дзержинский'), ('in', 'Индустриальный'), ('ki', 'Кировский'), ('le', 'Ленинский'), ('mo', 'Мотовилихинский'), ('or', 'Орджоникидзевский'), ('sv', 'Свердловский'))
RESUS = (('I+', 'Первая, положительный'), ('I-', 'Первая отрицательный'), ('II+', 'Вторая, положительный'), ('II-', ' Вторая отрицательный'), ('III+', 'Третья, положительный'), ('III-', 'Третья отрицательный'), ('IV+', 'Четвертая, положительный'), ('IV-', 'Четвертая отрицательный'))

class User(models.Model):
	username = models.CharField(unique=True, max_length=100, verbose_name = u'Никнейм')
	phone = models.CharField(unique=True, max_length=10, verbose_name = u'Номер телефона, без +7 или 8')
	surname = models.CharField(max_length=100, verbose_name = u'Фамилия')
	name = models.CharField(max_length=100, verbose_name = u'Имя')
	patronymic = models.CharField(max_length=100, blank=True, verbose_name = u'Отчество')
	date_of_birth  = models.DateField(verbose_name = u'Дата рождения, dd.mm.YYYY')
	gender = models.CharField(choices=GENDER, max_length=10, default='none', verbose_name = u'Пол')
	city = models.CharField(choices=CITY, max_length=20, default='perm', verbose_name = u'Город')
	district = models.CharField(max_length=20, choices=DISTRICT, blank=True, verbose_name = u'Район')
	street = models.CharField(max_length=20, verbose_name = u'Улица')
	building = models.CharField(max_length=20, verbose_name = u'Номер дома')
	room = models.IntegerField(max_length=4, verbose_name = u'Номер квартиры')
	invited_by = models.ForeignKey('self', verbose_name = u'Кто ответственный?')
	invite_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name = u'Когда пригласили?')
	is_active = models.BooleanField(default=True, verbose_name = u'Отсылать сообщения')
	is_admin = models.BooleanField(default=False, verbose_name = u'Администратор')
	password =  models.CharField(max_length=128, default='', blank=True, verbose_name = u'Пароль, если админ')
	penalty = models.IntegerField(default='0', verbose_name = u'Штрафные баллы (6 - отключен)')
	bike = models.CharField(max_length=100, blank=True, verbose_name = u'Марка-модель мотоцикла')
	bike_number = models.CharField(max_length=9, blank=True, verbose_name = u'Госномер мотоцикла')
	blood = models.CharField(choices=RESUS, max_length=4, blank=True, verbose_name = u'Группа крови, резус-фактор')
	relative_phone = models.CharField(max_length=10, blank=True, verbose_name = u'Телефон родственника')
	relative_name = models.CharField(max_length=255, blank=True, verbose_name = u'Как зовут родственника')

	def __unicode__(self):
        	return self.username

class EditForm(ModelForm):
     class Meta:
        model = User

class Message(models.Model):
	phone = models.CharField(max_length=11)
	sent = models.DateTimeField()
	received = models.DateTimeField()
	body = models.TextField()
	is_managed = models.BooleanField(default=False)
	my_id = models.CharField(unique=True, max_length=100)
