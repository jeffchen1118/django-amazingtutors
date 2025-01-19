from django.urls import path

from . import views

urlpatterns = [
    path("", views.LessonList.as_view(), name="home"),
    path("<slug:slug>/", views.lesson_detail, name="lesson_detail"),
]
