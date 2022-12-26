from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", include("django.contrib.auth.urls")),
    path("question/", views.QuestionListView.as_view(), name="questions-list"),
    path(
        "<slug>/",
        views.QuestionDetailView.as_view(),
        name="questions-detail",
    ),
]
