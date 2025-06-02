from rest_framework import serializers
from .models import Subtask

class SubtaskSerializer(serializers.ModelSerializer):

 class Meta:
  model = Subtask 
  fields = '__all__'

class UpdateSubtaskSerializer(serializers.ModelSerializer):
  
  class Meta:
   model = Subtask 
   fields = '__all__'