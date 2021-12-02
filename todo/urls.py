from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from todo.todoListViewSet import TodoListViewSet

router = DefaultRouter()

router.register('todo-list', TodoListViewSet)

urlpatterns = [
    url(r'todo', include(router.urls)),

]