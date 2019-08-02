from .models import Parent,Child
from django.views.generic import ListView


class ParentListView(ListView):
    model = Parent
    template_name = 'parent_list.html'
    context_object_name = 'parent_objects_list'


class ChildListView(ListView):
    model = Child
    template_name = 'child_list.html'
    context_object_name = 'child_objects_list'
    queryset = Parent.objects.prefetch_related('child')