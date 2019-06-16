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
        )


