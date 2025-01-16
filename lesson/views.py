from django.views import generic

from .models import Lesson


# Create your views here.
class LessonList(generic.ListView):
    """
    Displays the home page.
    """

    queryset = Lesson.objects.all()
    template_name = "lesson_list.html"
    paginate_by = 3
