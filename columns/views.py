from .models import Column
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics  
from django.shortcuts import get_object_or_404 
from .serializers import ColumnSerializer , UpdateColumnSerializer


# API endpoint to create a column or retrieve all columns
class CreateAndGetAllColumns(generics.ListCreateAPIView): 
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    
    
# API endpoint to retrieve a single column by id
class GetColumn(APIView):

    def get(self, request, id):
      
            column = get_object_or_404(Column , id = id )
            serializer = ColumnSerializer(column)
            
            return Response(serializer.data , status=status.HTTP_200_OK)

    
# API endpoint to retrieve columns using board id 
class GetColumnsByBoardId(APIView):

    def get(self, request, board_id):

            columns = Column.objects.filter(board_id = board_id)
            serializer = ColumnSerializer(columns , many=True)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
            
  
# API endpoint to delete a column using id 
class DeleteColumn(APIView):
  def delete(self , request , id) :
   
   column = get_object_or_404( Column, id = id )
   column.delete()
   
   return Response(
        {"message": "column deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)
  
  
# API endpoint to update a column by id
class UpdateColumn(APIView):
    def put(self, request, id):
       
        column = get_object_or_404( Column , id = id )
        serializer = UpdateColumnSerializer(column , data = request.data)
        
        if serializer.is_valid():
        
           serializer.save()
          
           return Response(serializer.data , status = status.HTTP_200_OK)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

