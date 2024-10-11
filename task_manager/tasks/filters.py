import django_filters
from task_manager.tasks.models import Tasks


class MyFilter(django_filters.FilterSet):
    class Meta:
        model = Tasks
        fields = ['status', 'executor']
