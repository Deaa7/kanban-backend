from .models import Subtask
from tasks.models import Task
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics  
from django.shortcuts import get_object_or_404 
from .serializers import SubtaskSerializer ,UpdateSubtaskSerializer

# API endpoint to create a subtask or retrieve all subtasks
class CreateAndGetAllSubtasks(generics.ListCreateAPIView): 
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
    
    
# API endpoint to retrieve a single subtask by id
class GetSubtask(APIView):

    def get(self, request, id):
        try:
            subtask = get_object_or_404(Subtask, id = id )
            serializer = SubtaskSerializer(subtask)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
            
        except Exception as e:
            
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
    
# API endpoint to retrieve subtasks using task id 
class GetSubtasksByTaskId(APIView):

    def get(self, request, task_id):

            subtasks = Subtask.objects.filter(task_id = task_id)
            serializer = SubtaskSerializer(subtasks , many=True)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
            
  
# API endpoint to delete a subtask using id
class DeleteSubtask(APIView):
  def delete(self , request , id) :
   
   subtask = get_object_or_404( Subtask, id = id )
   subtask.delete()
   
   return Response(
        {"message": "subtask deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)
  
  
# API endpoint to update a subtask by id
class UpdateSubtask(APIView):
    def put(self, request, id):
       
        subtask = get_object_or_404( Subtask , id = id )
        serializer = UpdateSubtaskSerializer(subtask , data = request.data)
        
        if serializer.is_valid():
        
           serializer.save()
           return Response(serializer.data , status = status.HTTP_200_OK)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def increaseNumberOfTaskSubtasks(request , task_id) :
    task = get_object_or_404(Task , id = task_id )
    task.number_of_subtasks += 1
    task.save()
    return Response("increase done successfully" , status = status.HTTP_200_OK)
    
@api_view(['POST'])
def decreaseNumberOfTaskSubtasks(request , task_id) :
    task = get_object_or_404(Task , id = task_id )
    task.number_of_subtasks += 1
    task.save()
    return Response("decrease done successfully" , status = status.HTTP_200_OK)

@api_view(['POST'])
def increaseNumberOfTaskCompletedSubtasks(request , task_id) :
    task = get_object_or_404(Task , id = task_id )
    task.number_of_completed_subtasks += 1
    task.save()
    return Response("increase done successfully" , status = status.HTTP_200_OK)
    
@api_view(['POST'])
def decreaseNumberOfTaskCompletedSubtasks(request , task_id) :
    task = get_object_or_404(Task , id = task_id )
    task.number_of_completed_subtasks += 1
    task.save()
    return Response("decrease done successfully" , status = status.HTTP_200_OK)
