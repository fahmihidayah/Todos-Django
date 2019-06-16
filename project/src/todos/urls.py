from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'todo', api.TodoViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Todo
    path('todos/todo/', views.TodoListView.as_view(), name='todos_todo_list'),
    path('todos/todo/create/', views.TodoCreateView.as_view(), name='todos_todo_create'),
    path('todos/todo/detail/<slug:slug>/', views.TodoDetailView.as_view(), name='todos_todo_detail'),
    path('todos/todo/update/<slug:slug>/', views.TodoUpdateView.as_view(), name='todos_todo_update'),
    path('todos/todo/delete/<slug:slug>/', views.TodoDeleteView.as_view(), name='todos_todo_delete'),
)

