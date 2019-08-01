from django import forms
from .models import Todo, Project, Comment


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status', 'user', 'project']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'todo', 'user']


