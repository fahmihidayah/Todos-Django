from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView
from .models import Todo, Project, Comment
from .forms import TodoForm, ProjectForm, CommentForm
from . import tables
import django_tables2
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from helper.query_help import get_parameter


class TodoListView(LoginRequiredMixin, django_tables2.SingleTableView):
    model = Todo
    paginate_by = 10
    table_class = tables.TodoTable

    extra_context = {'form': forms.SearchForm()}

    def get_queryset(self):
        query = self.model.objects.filter(user=self.request.user)
        project_id = get_parameter(self.kwargs, 'project_id', -1)

        if project_id != -1:
            query = query.filter(project__id=project_id)

        query = query.filter(title__icontains=get_parameter(self.request.GET, 'search', ''))

        status = get_parameter(self.request.GET, 'status', '0')
        if status != '0':
            query = query.filter(status=status)
        return query


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



class ProjectListView(LoginRequiredMixin, django_tables2.SingleTableView):
    model = Project
    paginate_by = 10
    table_class = tables.ProjectTable


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm

    def get_form(self, form_class=None):
        form: ProjectForm = super(ProjectCreateView, self).get_form(form_class)
        form.user = self.request.user
        return form


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class ProjectDeleteView(LoginRequiredMixin, DeleteView):

    def get_success_url(self):
        messages.success(
            self.request,
            "Data successful deleted",)
        return reverse_lazy('todos_project_list')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm


class CommentListView(ListView):
    model = Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm


class CommentDetailView(DetailView):
    model = Comment


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm

