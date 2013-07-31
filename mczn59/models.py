# ~*~ coding: utf-8 ~*~

from django.db import models
from django.contrib import admin

import datetime
from django.utils import timezone

from django.forms import ModelForm

import os
import uuid
def get_photo_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('photo', filename)

def get_anketa_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('anketa', filename)

# Create your models here.

GENDER = (('none', 'Не определен'), ('male', 'Мужчина'), ('female', 'Женщина'))
CITY = (('perm', 'Пермь'), ('krasnokamsk', 'Краснокамск'), ('berez', 'Березники'), ('dobr', 'Добрянка'), ('pol', 'Полазна'))
DISTRICT = (('dz', 'Дзержинский'), ('in', 'Индустриальный'), ('ki', 'Кировский'), ('le', 'Ленинский'), ('mo', 'Мотовилихинский'), ('or', 'Орджоникидзевский'), ('sv', 'Свердловский'))
RESUS = (('I+', 'Первая, положительный'), ('I-', 'Первая отрицательный'), ('II+', 'Вторая, положительный'), ('II-', ' Вторая отрицательный'), ('III+', 'Третья, положительный'), ('III-', 'Третья отрицательный'), ('IV+', 'Четвертая, положительный'), ('IV-', 'Четвертая отрицательный'))

class User(models.Model):
	username = models.CharField(unique=True, max_length=100, verbose_name = u'Никнейм')
	phone = models.CharField(unique=True, max_length=10, verbose_name = u'Телефон')
	surname = models.CharField(max_length=100, verbose_name = u'Фамилия')
	name = models.CharField(max_length=100, verbose_name = u'Имя')
	patronymic = models.CharField(max_length=100, blank=True, verbose_name = u'Отчество')
	date_of_birth  = models.DateField(verbose_name = u'Дата рождения, dd.mm.YYYY')
	gender = models.CharField(choices=GENDER, max_length=10, default='none', verbose_name = u'Пол')
	city = models.CharField(choices=CITY, max_length=20, default='perm', blank=True, verbose_name = u'Город')
	district = models.CharField(max_length=20, choices=DISTRICT, blank=True, verbose_name = u'Район')
	street = models.CharField(max_length=20, blank=True, verbose_name = u'Улица')
	building = models.CharField(max_length=20, blank=True, verbose_name = u'Номер дома')
	room = models.IntegerField(max_length=4, blank=True, verbose_name = u'Номер квартиры')
	invited_by = models.ForeignKey('self', verbose_name = u'Кто добавил?')
	invite_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name = u'Когда пригласили?')
	is_active = models.BooleanField(default=True, verbose_name = u'Обрабатывать его сообщения')
	add_new = models.BooleanField(default=True, verbose_name = u'Может добавлять новых')
	penalty = models.BooleanField(default=False, verbose_name = u'Проштрафился')
	bike = models.CharField(max_length=100, blank=True, verbose_name = u'Марка-модель мотоцикла')
	bike_number = models.CharField(max_length=9, blank=True, verbose_name = u'Госномер мотоцикла')
	blood = models.CharField(choices=RESUS, max_length=4, blank=True, verbose_name = u'Группа крови, резус-фактор')
	relative_phone = models.CharField(max_length=10, blank=True, verbose_name = u'Телефон родственника')
	relative_name = models.CharField(max_length=255, blank=True, verbose_name = u'Как зовут родственника')
	photo = models.FileField(upload_to=get_photo_path,
                        null=True,
                        blank=True,
                        verbose_name=(u'Фотоморда'))
	anketa = models.FileField(upload_to=get_anketa_path,
                        null=True,
                        blank=True,
                        verbose_name=(u'Скан анкеты'))
	codename = models.CharField(max_length=255, blank=True, verbose_name = u'Кодовое слово')
	def __unicode__(self):
        	return self.username

class Message(models.Model):
	phone = models.CharField(max_length=11, verbose_name = u'Номер телефона')
	sent = models.DateTimeField(verbose_name = u'Отправлено')
	received = models.DateTimeField(verbose_name = u'Принято')
	body = models.TextField(verbose_name = u'Текст SMS')
	is_managed = models.BooleanField(default=False, verbose_name = u'Обработано')
	my_id = models.CharField(unique=True, max_length=100)
	def __unicode__(self):
        	return self.body
