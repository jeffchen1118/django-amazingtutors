from django.urls import path

from lesson.views import my_lesson

urlpatterns = [
    # path("", views.HomePage.as_view(), name="home"),
    path("lesson/", my_lesson, name="lesson"),
]
