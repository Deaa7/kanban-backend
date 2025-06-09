from django.db import models
from columns.models import Column
from board.models import Board
# Create your models here.

class Task(models.Model) :
 board_id = models.ForeignKey(Board , on_delete=models.CASCADE , default = 1)
 column_id = models.ForeignKey(Column , on_delete=models.CASCADE)
 name = models.CharField(max_length=200 , default="")
 description = models.TextField(default="" , max_length = 2000 , blank =True)
 number_of_subtasks = models.IntegerField(default = 0 )
 number_of_completed_subtasks = models.IntegerField(default=0 )
#  status = models.CharField(max_length=200 , default="")
 def __str__(self):
  return self.name
 

 
 