from django.contrib import admin
from mczn59.models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'phone', 'surname', 'name', 'patronymic')

admin.site.register(User, UserAdmin)