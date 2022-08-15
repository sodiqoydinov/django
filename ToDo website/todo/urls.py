from urllib.parse import urlparse
from django.urls import path
from .views import index, addTodo, completeTodo, deleteComplited, deleteAll
urlpatterns = [
    path('', index, name='index'),
    path('add', addTodo, name='add'),
    path('complete/<todo_id>', completeTodo, name='complete'),
    path('delete_complited/', deleteComplited, name='delcom'),
    path('delete_all/', deleteAll, name='delall')
]
