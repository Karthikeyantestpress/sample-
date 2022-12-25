from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages


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


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = "clarifyit/question_form.html"
    fields = ["title", "slug", "description"]
    success_url = reverse_lazy("questions-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your question has been added")
        return super().form_valid(form)


class AnswerListView(LoginRequiredMixin, ListView):
    model = Answer
    template_name = "clarifyit/Answers.html"
