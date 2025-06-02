from django.urls import path
from . import views


urlpatterns = [
    
    path('create-board/', views.CreateAndGetAllBoard.as_view() ,name="create-board"), # creates a new board 
    
    path('get-all-boards/', views.CreateAndGetAllBoard.as_view() ,name="get-all-boards"), # gets all boards
    
    path('get-board/<int:id>/', views.GetBoard.as_view() ,name="get-board"), # gets single board using id 
 
    path('count-all-boards/', views.CountAllBoards.as_view() ,name="count-all-boards"), # count all boards 
 
    path('delete-board/<int:id>/', views.DeleteBoard.as_view() , name="delete-board"), # deletes board using id 
    
    path('update-board/<int:id>/', views.UpdateBoard.as_view() ,name="update-board"), # updates board using id 

]
