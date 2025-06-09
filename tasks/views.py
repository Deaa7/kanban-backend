from .models import Task
from columns.models import Column
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics  
from django.shortcuts import get_object_or_404 
from .serializers import TaskSerializer , UpdateTaskSerializer


# API endpoint to create a task or retrieve all tasks
class CreateAndGetAllTasks(generics.ListCreateAPIView): 
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# API endpoint to retrieve a single task by id
class GetTask(APIView):

    def get(self, request, id):
            task = get_object_or_404(Task, id = id )
            serializer = TaskSerializer(task)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
            
    
# API endpoint to retrieve tasks using board id 
class GetTasksByBoardId(APIView):

    def get(self, request, board_id):

            tasks = Task.objects.filter( board_id = board_id)
            serializer = TaskSerializer(tasks , many=True)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
            
# API endpoint to retrieve tasks using column id   
class GetTasksByColumnId(APIView):

    def get(self, request, column_id):

            tasks = Task.objects.filter( column_id = column_id)
            serializer = TaskSerializer(tasks , many=True)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
            
  
# API endpoint to delete a task using id (task_id)
class DeleteTask(APIView):
  def delete(self , request , id) :
   
   task = Task.objects.get(id = id)
   task.delete()
   return Response(
        {"message": "task deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)
  
  
# API endpoint to update a board by id
class UpdateTask(APIView):
    def put(self, request, id):
       
        task = get_object_or_404( Task , id = id )
        serializer = UpdateTaskSerializer(task , data = request.data)
        
        if serializer.is_valid():
        
           serializer.save()
           return Response(serializer.data , status = status.HTTP_200_OK)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def increaseNumberOfColumnTasks(request , column_id) :
    column = get_object_or_404(Column , id = column_id )
    column.number_of_tasks += 1
    column.save()
    return Response("increase done successfully" , status = status.HTTP_200_OK)
    
@api_view(['POST'])
def decreaseNumberOfColumnTasks(request , column_id) :
    column = get_object_or_404(Column , id = column_id )
    column.number_of_tasks -= 1
    column.save()
    return Response("decrease done successfully" , status = status.HTTP_200_OK)
