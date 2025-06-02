from django.db import models
from columns.models import Column
# Create your models here.

class Task(models.Model) :
 column_id = models.ForeignKey(Column , on_delete=models.CASCADE)
 name = models.CharField(max_length=200 , default="")
 description = models.TextField(default="" , max_length = 2000)
 number_of_subtasks = models.IntegerField(default = 0 , editable=False)
 number_of_completed_subtasks = models.IntegerField(default=0 , editable=False)
 status = models.CharField(max_length=200 , default="")
 def __str__(self):
  return self.name
 

 
 