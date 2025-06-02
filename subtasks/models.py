from django.db import models
from tasks.models import Task
# Create your models here.

class Subtask(models.Model) :
 task_id = models.ForeignKey(Task , on_delete=models.CASCADE)
 name = models.CharField(max_length=200 , default="")
 is_done = models.BooleanField(default=False)

 
 