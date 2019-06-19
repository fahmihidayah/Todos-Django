from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Todo
from .forms import TodoForm
from . import tables
import django_tables2
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect

class TodoListView(LoginRequiredMixin, django_tables2.SingleTableView):
    model = Todo
    paginate_by = 10
    table_class = tables.TodoTable

    extra_context = {'form': forms.SearchForm()}

    def get_queryset(self):
        try:
            keyword = self.request.GET['search']
            return self.model.objects.filter(user=self.request.user).filter(title__icontains=keyword)
        except:
            return self.model.objects.filter(user=self.request.user)

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm

    def get_form(self, form_class=None):
        form: TodoForm = super(TodoCreateView, self).get_form(form_class)
        form.user = self.request.user
        return form

    def get_success_url(self):
        return reverse_lazy('todos_todo_list')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse_lazy('todos_todo_list')


class TodoDetailView(LoginRequiredMixin,DetailView):
    model = Todo


class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = Todo
    form_class = TodoForm

    def get_form(self, form_class=None):
        form: TodoForm = super(TodoUpdateView, self).get_form(form_class)
        form.user = self.request.user
        return form

    def get_success_url(self):
        return reverse_lazy('todos_todo_list')

