from django.urls import path

from .views import (
    ParentListView,
    ChildListView
)

urlpatterns = [
    path('parents/', ParentListView.as_view(), name='parents'),
    path('childs/', ChildListView.as_view(), name='childs'),
]
