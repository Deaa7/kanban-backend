from django.contrib import admin
from .models import Subtask
# Register your models here.
 
 
class SubtaskAdmin(admin.ModelAdmin): 
    list_display = ['name' , 'task_id' , 'is_done' ]
    search_fields = ['name' ,'is_done']

admin.site.register(Subtask ,SubtaskAdmin)
