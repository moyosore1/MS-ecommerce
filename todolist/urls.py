from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.home, name='Todolist-home'),
    path('addtolist/', views.add_to_list, name='Todolist-add'),
    path('delete/', views.delete_from_list, name='Todolist-delete'),
    
]
