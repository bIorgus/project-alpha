from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project

# from django.urls.base import reverse_lazy, reverse


# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "list_of_projects"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project_detail"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    context_object_name = "project_create"
    fields = ["name", "description", "members"]

    def form_valid(self, form):
        item = form.save()
        item.owner = self.request.user
        item.save()
        return redirect("show_project", self)

    # should redirect to detail for newly created project,
    # moving on for now 6/23 18:35

    # def get_success_url(self, request):
    #     # return reverse_lazy("show_project", pk=self.kwargs["pk"])
    #     return reverse("show_project", args=request.pk)
