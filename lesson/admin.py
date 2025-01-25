from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Answer, Lesson, Note, Question

# Register your models here.


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    list_display = ("lesson", "user", "updated_on")
    search_fields = ["lesson", "body"]
    summernote_fields = ("body",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("lesson", "owner", "created_on")
    search_fields = ["lesson", "body"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "owner", "created_on")
    search_fields = ["question", "body"]
