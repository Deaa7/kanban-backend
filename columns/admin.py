from django.contrib import admin
from .models import Column
# Register your models here.
 
 
class ColumnAdmin(admin.ModelAdmin): 
    list_display = ['name' , 'board_id' , 'id' , 'number_of_tasks']
    search_fields = ['name' ,'board_id']

admin.site.register(Column ,ColumnAdmin)
