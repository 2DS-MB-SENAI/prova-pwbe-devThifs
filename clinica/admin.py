from django.contrib import admin
from .models import Consulta, Medico
from django.contrib.auth.admin import UserAdmin

admin.site.register(Consulta)
admin.site.register(Medico)

# Register your models here.
