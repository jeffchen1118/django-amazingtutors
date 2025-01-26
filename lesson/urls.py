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
    path(
        "<slug:slug>/question_edit/<int:id>",
        views.question_edit,
        name="question_edit",
    ),
    path(
        "<slug:slug>/question_delete/<int:id>",
        views.question_delete,
        name="question_delete",
    ),
    path(
        "<slug:slug>/answer_create/<int:id>", views.answer_create, name="answer_create"
    ),
    path(
        "<slug:slug>/answer_edit/<int:id>",
        views.answer_edit,
        name="answer_edit",
    ),
    path(
        "<slug:slug>/answer_delete/<int:id>",
        views.answer_delete,
        name="answer_delete",
    ),
    path(
        "<slug:slug>/grade_feedback/<int:id>",
        views.grade_feedback,
        name="grade_feedback",
    ),
    path("", views.LessonList.as_view(), name="home"),
]
