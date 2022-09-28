from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Task
from django.urls import reverse_lazy


# Create your views here.
class HomePageView(ListView):
    model = Task
    template_name = "home.html"


class CreateTaskPageView(CreateView):
    model = Task
    template_name = "create_task.html"
    fields = (
        "title",
        "info",
    )
