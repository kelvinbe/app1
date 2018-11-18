from todo.models import Todolist
from rest_framework import viewsets
from .todo import TodolistSerializer

class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Todolist,objects.all()
    serializer_class = TodolistSerializer
