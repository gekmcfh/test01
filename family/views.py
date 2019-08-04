from .models import Parent,Child
from django.views.generic import ListView
from django.db.models import Prefetch


class ParentListView(ListView):
    model = Parent
    template_name = 'child_list.html'
    context_object_name = 'parent_objects_list'


class ChildListView(ListView):
    model = Parent
    template_name = 'child_list.html'
    context_object_name = 'parent_child_objects_list'
    queryset = Parent.objects.prefetch_related(Prefetch('child_set'))


# class GChildListView(ListView):
#     model = Child
#     template_name = 'gchild_list.html'
#     context_object_name = 'child_objects_list'
#     queryset = Parent.objects.prefetch_related(Prefetch('child_set')).all()
