from django.contrib import admin
from .models import Task
# Register your models here.
 
 
class TaskAdmin(admin.ModelAdmin): 
    list_display = ['name'   , 'id' , 'number_of_subtasks','number_of_completed_subtasks']
    search_fields = ['name' ]

admin.site.register(Task ,TaskAdmin)
