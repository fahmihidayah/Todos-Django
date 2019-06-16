from django.contrib import admin
from django import forms
from .models import Todo

class TodoAdminForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'


class TodoAdmin(admin.ModelAdmin):
    form = TodoAdminForm
    list_display = ['title', 'slug', 'created', 'last_updated', 'description']
    readonly_fields = ['title', 'slug', 'created', 'last_updated', 'description']

admin.site.register(Todo, TodoAdmin)


