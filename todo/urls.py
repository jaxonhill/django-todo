from django.urls import path, include
from .views import HomePageView, CreateTaskPageView, EditTaskPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("create/", CreateTaskPageView.as_view(), name="create"),
    path("edit/<int:pk>/", EditTaskPageView.as_view(), name="edit"),
]
