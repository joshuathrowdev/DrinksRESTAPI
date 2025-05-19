from django.contrib import admin

# Imported Models
from .models import Drink

@admin.register(Drink)
class DrinksAdmin(admin.ModelAdmin):
  list_display = ['name', 'description']