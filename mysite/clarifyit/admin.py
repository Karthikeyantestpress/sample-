from django.contrib import admin
from .models import Question, Answer, Comment


@admin.register(Question)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    list_filter = ("created", "author")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "created"
    ordering = ("created",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "question", "created", "active")
    list_filter = ("active", "created", "updated")
    search_fields = ("name", "email", "body")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "answer", "created", "active")
    list_filter = ("active", "created", "updated")
    search_fields = ("name", "email", "body")
