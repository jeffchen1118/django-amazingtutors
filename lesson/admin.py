from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Answer, GradeFeedback, Lesson, Note, Question

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
class QuestionAdmin(SummernoteModelAdmin):
    list_display = ("lesson", "owner", "created_on")
    search_fields = ["lesson", "body"]
    summernote_fields = ("body",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "owner", "created_on")
    search_fields = ["question", "body", "grade", "feedback"]


@admin.register(GradeFeedback)
class GradeFeedbackAdmin(admin.ModelAdmin):
    list_display = ("answer", "grade", "feedback")
    search_fields = ["answer", "grade", "feedback"]
    summernote_fields = ("feedback",)
