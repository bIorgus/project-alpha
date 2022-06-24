from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task


# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template = "tasks/task_form.html"
    context_object_name = "task_create"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def form_valid(self, form):
        item = form.save()
        item.owner = self.request.user
        item.save()
        return redirect("home")

    # def get_success_url(self):
    #     return redirect("home")

    # this should redirect to the detail view of the project for which
    # the task was created, but i can't figure that out quickly enough
    # so it will redirect to home for now
