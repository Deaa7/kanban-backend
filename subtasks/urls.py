from django.urls import path
from . import views


urlpatterns = [
    
    path('create-subtask/', views.CreateAndGetAllSubtasks.as_view() , name="create-subtask"), # creates a new subtask 
    
    path('get-all-subtasks-by-task-id/<int:task_id>/', views.GetSubtasksByTaskId.as_view() ,name="get-all-subtask-by-task-id"), # get all subtasks by task id
    
    path('get-subtask/<int:id>/', views.GetSubtask.as_view() ,name="get-subtask"), # gets single subtask using id 
 
    path('delete-subtask/<int:id>/', views.DeleteSubtask.as_view() , name="delete-subtask"), # deletes subtask using id 
    
    path('update-subtask/<int:id>/', views.UpdateSubtask.as_view() ,name="update-subtask"), # updates subtask using id 

    path('increase-number-of-task-subtasks/<int:task_id>/', views.increaseNumberOfTaskSubtasks ,name="increase-number-of-task-subtasks"), # increase number of task subtasks

    path('decrease-number-of-task-subtasks/<int:task_id>/', views.decreaseNumberOfTaskSubtasks ,name="decrease-number-of-task-subtasks"), # decrease number of task subtasks

    path('increase-number-of-task-completed-subtasks/<int:task_id>/', views.increaseNumberOfTaskCompletedSubtasks ,name="increase-number-of-task-completed-subtasks"), # increase number of task completed subtasks

    path('decrease-number-of-task-completed-subtasks/<int:task_id>/', views.decreaseNumberOfTaskCompletedSubtasks ,name="decrease-number-of-task-completed-subtasks"), #  decrease number of task completed subtasks

]
