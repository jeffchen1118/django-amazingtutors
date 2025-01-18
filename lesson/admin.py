from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Lesson, Lesson_section, Note

# Register your models here.


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


@admin.register(Lesson_section)
class Lesson_sectionAdmin(SummernoteModelAdmin):
    list_display = ("title", "lesson", "order")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    list_display = ("title", "author", "created_on")
    search_fields = ["title", "body"]
    summernote_fields = ("body",)
