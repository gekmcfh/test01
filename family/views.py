from .models import Parent,Child
from django.views.generic import ListView
from django.db.models import Prefetch


class ParentListView(ListView):
    model = Parent
    template_name = 'parent_list.html'
    context_object_name = 'parent_objects_list'


class ChildListView(ListView):
    model = Parent
    template_name = 'child_list.html'
    context_object_name = 'parent_objects_list'
    queryset = Parent.objects.prefetch_related(Prefetch('child_set'))



