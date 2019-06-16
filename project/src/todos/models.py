from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
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

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="todos", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    @property
    def get_list_url(self):
        return reverse('todos_todo_list')

    @property
    def get_absolute_url(self):
        return reverse('todos_todo_detail', args=(self.slug,))

    @property
    def get_update_url(self):
        return reverse('todos_todo_update', args=(self.slug,))

    @property
    def get_delete_url(self):
        return reverse('todos_todo_delete', args=(self.slug,))




