from django.contrib import admin

from .models import Lesson

# Register your models here.
# admin.site.register(Lesson)
# admin.site.register(Lesson_section)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
