from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    