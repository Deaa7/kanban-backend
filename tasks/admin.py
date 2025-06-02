from django.contrib import admin
from .models import Task
# Register your models here.
 
 
class TaskAdmin(admin.ModelAdmin): 
    list_display = ['name' , 'status' , 'id' , 'number_of_subtasks','number_of_completed_subtasks']
    search_fields = ['name' ,'status']

admin.site.register(Task ,TaskAdmin)
