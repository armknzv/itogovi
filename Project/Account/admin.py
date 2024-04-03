from django.contrib import admin

from .models import *


class User_AuthlAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_auth', 'role_auth', )


admin.site.register(User_Auth, User_AuthlAdmin)