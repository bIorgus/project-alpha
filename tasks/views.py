from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
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


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template = "tasks/list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template = "tasks/list.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
