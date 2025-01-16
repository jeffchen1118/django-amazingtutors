from django.urls import path

from . import views

urlpatterns = [
    path("", views.LessonList.as_view(), name="home"),
    # path("lesson/", my_lesson, name="lesson"),
]
