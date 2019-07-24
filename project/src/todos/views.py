from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView
from .models import Todo
from .forms import TodoForm
from . import tables
import django_tables2
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


class TodoListView(LoginRequiredMixin, django_tables2.SingleTableView):
    model = Todo
    paginate_by = 10
    table_class = tables.TodoTable

    extra_context = {'form': forms.SearchForm()}

    def get_queryset(self):
        try:
            keyword = self.request.GET['search']
            status = self.request.GET['status']
            if status == '0':
                return self.model.objects.filter(user=self.request.user).filter(title__icontains=keyword)
            else:
                return self.model.objects.filter(user=self.request.user).filter(title__icontains=keyword).filter(status=status)
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
        messages.success(
            self.request,
            "Data successful created", )
        return reverse_lazy('todos_todo_list')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo

    def get_success_url(self):
        messages.success(
            self.request,
            "Data successful deleted",)
        return reverse_lazy('todos_todo_list')


class TodoDetailView(LoginRequiredMixin,DetailView):
    model = Todo

    def get_context_data(self, **kwargs):
        context = super(TodoDetailView, self).get_context_data()
        context.update({'form': forms.TodoUpdateStatusForm()})
        return context


class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = Todo
    form_class = TodoForm

    def get_form(self, form_class=None):
        form: TodoForm = super(TodoUpdateView, self).get_form(form_class)
        form.user = self.request.user
        return form

    def get_success_url(self):
        messages.success(
            self.request,
            "Data successful updated", )
        return reverse_lazy('todos_todo_list')


class TodoUpdateDoneView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = forms.TodoUpdateStatusForm

    def get_form(self, form_class=None):
        form: TodoForm = super(TodoUpdateDoneView, self).get_form(form_class)
        form.user = self.request.user
        return form

    def get_success_url(self):
        messages.success(
            self.request,
            "Success change status", )
        return reverse_lazy('todos_todo_list')



class TestView(TemplateView):
    template_name = "test_template.html"