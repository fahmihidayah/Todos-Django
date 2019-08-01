from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Todo(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=225)
    status = models.BooleanField()

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="todos", 
    )
    project = models.ForeignKey(
        'todos.Project',
        on_delete=models.CASCADE, related_name="todos", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('todos_todo_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('todos_todo_update', args=(self.slug,))


class Project(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('todos_project_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('todos_project_update', args=(self.slug,))


class Comment(models.Model):

    # Fields
    text = models.TextField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    todo = models.ForeignKey(
        'todos.Todo',
        on_delete=models.CASCADE, related_name="comments", 
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="comments", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('todos_comment_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('todos_comment_update', args=(self.slug,))


