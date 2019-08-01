import unittest
from django.urls import reverse
from django.test import Client
from .models import Todo, Project, Comment
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_todo(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["description"] = "description"
    defaults["status"] = "status"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "project" not in defaults:
        defaults["project"] = create_project()
    return Todo.objects.create(**defaults)


def create_project(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Project.objects.create(**defaults)


def create_comment(**kwargs):
    defaults = {}
    defaults["text"] = "text"
    defaults.update(**kwargs)
    if "todo" not in defaults:
        defaults["todo"] = create_todo()
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Comment.objects.create(**defaults)


class TodoViewTest(unittest.TestCase):
    '''
    Tests for Todo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_todo(self):
        url = reverse('todos_todo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        url = reverse('todos_todo_create')
        data = {
            "title": "title",
            "description": "description",
            "status": "status",
            "user": create_django_contrib_auth_models_user().pk,
            "project": create_project().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_todo(self):
        todo = create_todo()
        url = reverse('todos_todo_detail', args=[todo.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_todo(self):
        todo = create_todo()
        data = {
            "title": "title",
            "description": "description",
            "status": "status",
            "user": create_django_contrib_auth_models_user().pk,
            "project": create_project().pk,
        }
        url = reverse('todos_todo_update', args=[todo.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProjectViewTest(unittest.TestCase):
    '''
    Tests for Project
    '''
    def setUp(self):
        self.client = Client()

    def test_list_project(self):
        url = reverse('todos_project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_project(self):
        url = reverse('todos_project_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_project(self):
        project = create_project()
        url = reverse('todos_project_detail', args=[project.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_project(self):
        project = create_project()
        data = {
            "name": "name",
        }
        url = reverse('todos_project_update', args=[project.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CommentViewTest(unittest.TestCase):
    '''
    Tests for Comment
    '''
    def setUp(self):
        self.client = Client()

    def test_list_comment(self):
        url = reverse('todos_comment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_comment(self):
        url = reverse('todos_comment_create')
        data = {
            "text": "text",
            "todo": create_todo().pk,
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_comment(self):
        comment = create_comment()
        url = reverse('todos_comment_detail', args=[comment.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_comment(self):
        comment = create_comment()
        data = {
            "text": "text",
            "todo": create_todo().pk,
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('todos_comment_update', args=[comment.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


