from django.urls import path

from . import views

urlpatterns = [
    path("", views.LessonList.as_view(), name="home"),
    path("<slug:slug>/", views.lesson_detail, name="lesson_detail"),
    path("<slug:slug>/edit_note/<int:note_id>/", views.edit_note, name="edit_note"),
]
