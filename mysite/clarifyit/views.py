from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def default_page(request):
    return render(request, "base.html")


@login_required
def home(request):
    return render(request, "clarifyit/home.html")
