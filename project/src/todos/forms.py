from django import forms
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



