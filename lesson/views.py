from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
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

    lesson = get_object_or_404(Lesson, slug=slug)
    user_notes = Note.objects.filter(user=request.user, lesson=lesson)

    notes_dict = {note.lesson.id: note for note in user_notes}

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.lesson = lesson
            note.save()
            return redirect("lesson_detail", slug=slug)
    else:
        form = NoteForm()

    return render(
        request,
        "lesson/lesson_detail.html",
        {
            "lesson": lesson,
            "notes_dict": notes_dict,
            "note_form": form,
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
