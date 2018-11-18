from todo.models import Todolist
from rest_framework import serializers


class TodolistSerializer(serializers.ModelSerializer)
    class Meta:
        model = Todolist
        fields = ('title', 'content', 'created', 'due_date', 'category')
