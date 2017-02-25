from django.shortcuts import render
from django.views.generic.list import ListView

from management.models import Target, Test

class TargetListView(ListView):
    model = Target
    template_name = 'target_list.html'

class TestListView(ListView):
    model = Test
    template_name = 'test_list.html'

    def get_queryset(self):
        target_id =  int(self.kwargs['pk'])
        target = Target.objects.filter(id=target_id)
        self.object_list = Test.objects.filter(target=target)
        return self.object_list