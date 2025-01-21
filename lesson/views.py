from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic

from .forms import NoteForm
from .models import Lesson, Note


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
    lesson_sections = lesson.sections.all().order_by("order")

    if request.method == "POST":
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            # note.title = lesson_sections.get(id=request.POST.get("section_id"))
            note.author = request.user
            note.body = request.POST.get("body")
            note.save()

    note_form = NoteForm()

    notes = []
    for section in lesson_sections:
        notes.extend(section.notes.all().filter(author=request.user))

    return render(
        request,
        "lesson/lesson_detail.html",
        {
            "lesson": lesson,
            "lesson_sections": lesson_sections,
            "notes": notes,
            "note_form": note_form,
        },
    )


def edit_note(request, note_id):
    """
    Edit a :model:`lesson.Note`.

    **Context**

    ``note``
        An instance of :model:`lesson.Note`.

    **Template:**

    :template:`lesson/edit_note.html`
    """

    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        note_form = NoteForm(request.POST, instance=note)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.save()
            messages.success(request, "Note updated successfully.")
            return HttpResponseRedirect(
                reverse("lesson:lesson_detail", args=[note.title.lesson.slug])
            )

    note_form = NoteForm(instance=note)

    return render(
        request, "lesson/edit_note.html", {"note": note, "note_form": note_form}
    )
