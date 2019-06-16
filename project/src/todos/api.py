from . import models
from . import serializers
from rest_framework import viewsets, permissions


class TodoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Todo class"""

    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


