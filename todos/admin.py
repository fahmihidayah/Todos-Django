from django.contrib import admin
from django import forms
from .models import Todo, Project, Comment

class TodoAdminForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'


class TodoAdmin(admin.ModelAdmin):
    form = TodoAdminForm
    list_display = ['title', 'slug', 'created', 'last_updated', 'description', 'status']
    readonly_fields = ['title', 'slug', 'created', 'last_updated', 'description', 'status']

admin.site.register(Todo, TodoAdmin)


class ProjectAdminForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Project, ProjectAdmin)


class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ['text', 'slug', 'created', 'last_updated']
    readonly_fields = ['text', 'slug', 'created', 'last_updated']

admin.site.register(Comment, CommentAdmin)


