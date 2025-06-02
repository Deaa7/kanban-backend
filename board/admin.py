from django.contrib import admin
from .models import Board
# Register your models here.
 
 
class BoardAdmin(admin.ModelAdmin): 
    list_display = ['id' ,'name']
    search_fields = ['name']

admin.site.register(Board ,BoardAdmin)
