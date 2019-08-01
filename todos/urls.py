from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'todo', api.TodoViewSet)
router.register(r'project', api.ProjectViewSet)
router.register(r'comment', api.CommentViewSet)


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
)

urlpatterns += (
    # urls for Project
    path('todos/project/', views.ProjectListView.as_view(), name='todos_project_list'),
    path('todos/project/create/', views.ProjectCreateView.as_view(), name='todos_project_create'),
    path('todos/project/detail/<slug:slug>/', views.ProjectDetailView.as_view(), name='todos_project_detail'),
    path('todos/project/update/<slug:slug>/', views.ProjectUpdateView.as_view(), name='todos_project_update'),
)

urlpatterns += (
    # urls for Comment
    path('todos/comment/', views.CommentListView.as_view(), name='todos_comment_list'),
    path('todos/comment/create/', views.CommentCreateView.as_view(), name='todos_comment_create'),
    path('todos/comment/detail/<slug:slug>/', views.CommentDetailView.as_view(), name='todos_comment_detail'),
    path('todos/comment/update/<slug:slug>/', views.CommentUpdateView.as_view(), name='todos_comment_update'),
)

