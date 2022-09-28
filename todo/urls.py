from django.urls import path, include
from .views import HomePageView, CreateTaskPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("create/", CreateTaskPageView.as_view(), name="create"),
]
