from django.contrib import admin
from .models import Meseros
# Register your models here.

@admin.register(Meseros)
class MeserosAdmin(admin.ModelAdmin):
    list_display = ("pais","edad")
