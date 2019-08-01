from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Todo, Project, Comment
from .forms import TodoForm, ProjectForm, CommentForm


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm


class TodoDetailView(DetailView):
    model = Todo


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm


class ProjectListView(ListView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm


class ProjectDetailView(DetailView):
    model = Project


class ProjectUpdateView(UpdateView):
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

