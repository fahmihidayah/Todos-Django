from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Fieldset
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.urls import reverse

from .models import Todo, Project, Comment


class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.helper = FormHelper()

    def save(self, commit=True):
        model: Todo = super(TodoForm, self).save(commit=False)
        model.user = self.user
        model.save()
        return model

    class Meta:
        model = Todo
        fields = ['title', 'description', 'project']


class TodoUpdateStatusForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    def save(self, commit=True):
        model: Todo = super(TodoUpdateStatusForm, self).save(commit=False)
        model.user = self.user
        model.save()
        return model

    class Meta:
        model = Todo
        fields = ['status']


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.widgets.TextInput(attrs={"size": 35}))
    status = forms.ChoiceField(choices=[('0', 'All'),('1', 'New'), ('2', 'Done')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('search', css_class="form-control")
        )
        self.fields['search'].required = False



class ProjectForm(forms.ModelForm):

    def save(self, commit=True):
        model: Project = super(ProjectForm, self).save(commit=False)
        model.user = self.user
        model.save()
        return model

    class Meta:
        model = Project
        fields = ['name']


class CommentForm(forms.ModelForm):

    def save(self, commit=True):
        model: Comment = super(CommentForm, self).save(commit=False)
        model.user = self.user
        model.save()
        return model

    class Meta:
        model = Comment
        fields = ['text', 'todo', 'user']



