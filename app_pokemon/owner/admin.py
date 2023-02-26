from django.contrib import admin
from .models import Owner

# Register your models here.

#admin.site.register(Owner)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
   list_display = ("nombre","pais","edad")
   list_filter = ("pais","edad")
   search_fields = ("nombre",)
   fields = ("nombre","pais","edad","dni")

