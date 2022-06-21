from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project


# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "list_of_projects"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)
