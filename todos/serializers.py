from . import models

from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Todo
        fields = (
            'slug', 
            'title', 
            'created', 
            'last_updated', 
            'description', 
            'status', 
        )


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = (
            'slug', 
            'text', 
            'created', 
            'last_updated', 
        )


