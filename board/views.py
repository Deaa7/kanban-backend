from .models import Board
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics  
from django.shortcuts import get_object_or_404 
from .serializers import BoardSerializer , UpdateBoardSerializer


# API endpoint to create a board or retrieve all boards
class CreateAndGetAllBoard(generics.ListCreateAPIView): 
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
# API endpoint to count all boards
class CountAllBoards(APIView):

    def get(self, request):

            boards = Board.objects.all().count()
            return Response(boards, status=status.HTTP_200_OK)
            
     
# API endpoint to retrieve a single board by id
class GetBoard(APIView):

    def get(self, request, id):

        item = get_object_or_404(Board , id = id )
        serializer = BoardSerializer(item)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        

            

# API endpoint to delete a board using id 
class DeleteBoard(APIView):
  def delete(self , request , id) :
   
   board = get_object_or_404( Board, id = id )
   board.delete()
   
   return Response(
        {"message": "board deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)
  
  
# API endpoint to update a board by id
class UpdateBoard(APIView):
    def put(self, request, id):
       
        board = get_object_or_404(Board, id=id)
        serializer = UpdateBoardSerializer(board, data=request.data)
        
        if serializer.is_valid():
        
           serializer.save()
        
           return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

