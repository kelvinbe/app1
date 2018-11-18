from todos.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'content', 'created', 'due_date', 'category')
