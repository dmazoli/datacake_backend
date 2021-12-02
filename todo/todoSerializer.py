from rest_framework import serializers
from todo.todoModel import TodoModel

class TodoSerializer(serializers.Serializer):
    class Meta:
        model = TodoModel
        fields = '__all__'