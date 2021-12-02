from rest_framework import viewsets
from todo.todoModel import TodoModel
from todo.todoSerializer import TodoSerializer

class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()
    ordering_fields = ["-inicio"]