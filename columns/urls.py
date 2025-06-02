from django.urls import path
from . import views


urlpatterns = [
    
    path('create-column/', views.CreateAndGetAllColumns.as_view() ,name="create-column"), # creates a new column 
    
    path('get-all-columns-by-board-id/<int:board_id>/', views.GetColumnsByBoardId.as_view() ,name="get-all-columns-by-board-id"), # get all columns by board id
    
    path('get-column/<int:id>/', views.GetColumn.as_view() ,name="get-column"), # gets single column using id 
 
    path('delete-column/<int:id>/', views.DeleteColumn.as_view() , name="delete-column"), # deletes column using id 
    
    path('update-column/<int:id>/', views.UpdateColumn.as_view() ,name="update-column"), # updates column using id 

]
