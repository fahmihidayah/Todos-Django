from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.urls import reverse
from .models import Todo


class TodoForm(forms.ModelForm):

    def save(self, commit=True):
        model: Todo= super(TodoForm, self).save(commit=False)
        model.user = self.user
        model.save()
        return model

    class Meta:
        model = Todo
        fields = ['title', 'description']


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.widgets.TextInput(attrs={"size": 35}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('search', css_class="form-control")
        )



