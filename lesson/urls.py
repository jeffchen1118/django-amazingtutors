from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.lesson_create, name="lesson_create"),
    path("<slug:slug>/lesson_delete", views.lesson_delete, name="lesson_delete"),
    path("<slug:slug>/", views.lesson_detail, name="lesson_detail"),
    path(
        "<slug:slug>/lesson_edit/",
        views.lesson_edit,
        name="lesson_edit",
    ),
    path("<slug:slug>/question_create", views.question_create, name="question_create"),
    path("", views.LessonList.as_view(), name="home"),
]
