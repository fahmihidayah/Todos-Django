from . import models
from . import serializers
from rest_framework import viewsets, permissions


class TodoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Todo class"""

    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Project class"""

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Comment class"""

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


