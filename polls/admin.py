from django.contrib import admin
from polls.models import product
from polls.models import pollsuser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
admin.site.register(product)
admin.site.register(pollsuser)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'password', 'first_name', 'last_name')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
