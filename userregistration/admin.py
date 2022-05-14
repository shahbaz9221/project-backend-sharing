from django.contrib import admin
from userregistration.models import UserRegistration, AdminLogin
# Register your models here.

admin.site.register(UserRegistration)
admin.site.register(AdminLogin)
