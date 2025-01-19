from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Lesson


# Create your views here.
class LessonList(generic.ListView):
    """
    Displays the home page.
    """

    queryset = Lesson.objects.all()
    template_name = "lesson/index.html"
    paginate_by = 3


def lesson_detail(request, slug):
    """
    Display an individual :model:`lesson.Lesson`.

    **Context**

    ``lesson``
        An instance of :model:`lesson.Lesson`.

    **Template:**

    :template:`lesson/lesson_detail.html`
    """

    queryset = Lesson.objects.filter(status=1)
    lesson = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "lesson/lesson_detail.html",
        {"lesson": lesson},
    )
