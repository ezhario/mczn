from django.contrib import admin
from mczn59.models import User, Message

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'phone', 'surname', 'name', 'patronymic')
class UserSMS(admin.ModelAdmin)
    list_display = ('phone', 'sent', 'received', 'body', 'is_managed')

admin.site.register(User, UserAdmin, UserSMS)