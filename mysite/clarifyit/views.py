from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Question
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def default_page(request):
    return render(request, "base.html")


@login_required
def home(request):
    return render(request, "clarifyit/home.html")


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = "clarifyit/question_list.html"


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = "clarifyit/question_detail.html"
