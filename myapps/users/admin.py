from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['email', 'first_name', 'last_name', 'last_login']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
