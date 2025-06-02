from django.urls import path
from . import views


urlpatterns = [
    
    path('create-task/', views.CreateAndGetAllTasks.as_view() , name="create-task"), # creates a new task 
    
    path('get-all-tasks-by-column-id/<int:column_id>/', views.GetTasksByColumnId.as_view() ,name="get-all-tasks-by-column-id"), # get all tasks by column id
    
    path('get-task/<int:id>/', views.GetTask.as_view() ,name="get-task"), # gets single task using id 
 
    path('delete-task/<int:id>/', views.DeleteTask.as_view() , name="delete-task"), # deletes task using id 
    
    path('update-task/<int:id>/', views.UpdateTask.as_view() ,name="update-task"), # updates task using id 

    path('increase-number-of-column-tasks/<int:column_id>/', views.increaseNumberOfColumnTasks ,name="increase-number-of-column-tasks"), # increase number of column tasks 
    
    path('decrease-number-of-column-tasks/<int:column_id>/', views.decreaseNumberOfColumnTasks ,name="decrease-number-of-column-tasks"), # decrease number of column tasks
]
