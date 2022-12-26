from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="question"
    )
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "questions-detail",
            args=[
                self.slug,
            ],
        )


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Answered by {self.name} on {self.question}"


class Comment(models.Model):
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"commented by {self.name} on {self.answer}"
