from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("question/", views.QuestionListView.as_view(), name="questions-list"),
    path("", include("django.contrib.auth.urls")),
]
