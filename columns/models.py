from django.db import models
from board.models import Board
# Create your models here.

class Column(models.Model) :
 board_id = models.ForeignKey(Board , on_delete=models.CASCADE)
 name = models.CharField(max_length=200 , default="")
 number_of_tasks = models.IntegerField(db_default = 0  , editable=False)
 
 def __str__(self):
  return self.name
 