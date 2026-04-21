from django.urls import path
from .import views 

urlpatterns = [
    path('',views.todo_list,name="Todo_list"),
    path('add/',views.create_todo,name="add_todo"),
    path('delete/<int:id>/',views.delete_todo,name="delete_todo"),
    path('update/<int:id>',views.update_todo,name="update_todo"),
    path('toggle/<int:id>/',views.toggle_complete,name='toggle_complete'),
    path('signup/',views.signup,name='signup'),
]
