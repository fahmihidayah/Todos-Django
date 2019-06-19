import django_tables2 as tables
from .models import Todo

class TodoTable(tables.Table):
    edit = tables.TemplateColumn(template_name='todos/table/edit.html')

    delete = tables.TemplateColumn(template_name='todos/table/delete.html')

    detail = tables.TemplateColumn(template_name='todos/table/detail.html')
    class Meta:
        model = Todo
        fields = ['id', 'title', 'created']
        template_name = 'django_tables2/bootstrap.html'


