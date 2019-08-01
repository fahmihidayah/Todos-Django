import django_tables2 as tables
from .models import Todo, Project

class TodoTable(tables.Table):
    edit = tables.TemplateColumn(template_name='todos/table/edit.html')

    delete = tables.TemplateColumn(template_name='todos/table/delete.html')

    detail = tables.TemplateColumn(template_name='todos/table/detail.html')

    change_status = tables.TemplateColumn(template_name='todos/table/set_done.html')

    class Meta:
        model = Todo
        fields = ['id', 'title', 'status_str', 'created']
        template_name = 'django_tables2/bootstrap.html'



class ProjectTable(tables.Table):
    todo = tables.TemplateColumn(template_name='todos/table/project_list_todo.html')

    edit = tables.TemplateColumn(template_name='todos/table/edit.html')

    delete = tables.TemplateColumn(template_name='todos/table/delete.html')

    detail = tables.TemplateColumn(template_name='todos/table/detail.html')

    class Meta:
        model = Project
        fields = ['id', 'name', 'created', ]
        template_name = 'django_tables2/bootstrap.html'


