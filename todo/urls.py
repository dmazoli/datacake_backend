from django.urls import include, path
from rest_framework.routers import DefaultRouter

from todo.todoListViewSet import TodoListViewSet

router = DefaultRouter()

router.register('todo-list', TodoListViewSet, basename="todo-list")

urlpatterns = [
    path('', include(router.urls)),

]