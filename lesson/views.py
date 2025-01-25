from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, IntegerField, Value, When
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.text import slugify
from django.views import generic
from django.views.generic.edit import CreateView

from .forms import AnswerForm, LessonForm, NoteForm, QuestionForm
from .models import Answer, Lesson, Note, Question

# Create your views here.
# class LessonCreate(CreateView):
#     model = Lesson
#     form_class = LessonForm
#     template_name = "lesson/lesson_create.html"
#     success_url = "/"


class LessonList(generic.ListView):
    """
    Displays the home page.
    """

    template_name = "lesson/index.html"
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # If the user is authenticated, show all lessons if they are the author
            return Lesson.objects.filter(
                author=self.request.user
            ) | Lesson.objects.filter(status=1).order_by("-created_on")
        else:
            # If the user is not authenticated, show only published lessons
            return Lesson.objects.filter(status=1)


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
    if request.user.is_authenticated:  # Check if user is authenticated
        user_note = Note.objects.filter(user=request.user, lesson=lesson).first()

        # Annotate questions to prioritize author's questions
        questions = (
            Question.objects.filter(lesson=lesson)
            .annotate(
                is_author=Case(
                    When(owner=lesson.author, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                )
            )
            .order_by("-is_author", "created_on")
        )

    if request.method == "POST":
        form = NoteForm(request.POST, instance=user_note)
        if form.is_valid():
            note = form.save(commit=False)
            note.lesson = lesson
            note.body = form.cleaned_data["body"]
            note.user = request.user
            note.save()
            return redirect("lesson_detail", slug=slug)

    if request.user.is_authenticated:
        form = NoteForm(instance=user_note)
    else:
        form = NoteForm()

    return render(
        request,
        "lesson/lesson_detail.html",
        {
            "lesson": lesson,
            "questions": questions,
            "user_note": user_note,
            "note_form": form,
        },
    )


def lesson_edit(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    if request.method == "POST":
        lesson_form = LessonForm(request.POST, instance=lesson)
        if lesson_form.is_valid():
            lesson = lesson_form.save(commit=False)
            lesson.author = request.user
            lesson.save()
            messages.success(request, "Lesson updated successfully.")
            return HttpResponseRedirect(reverse("lesson_detail", args=[lesson.slug]))
    lesson_form = LessonForm(instance=lesson)
    return render(
        request,
        "lesson/lesson_edit.html",
        {"lesson": lesson, "lesson_form": lesson_form},
    )


def lesson_create(request):
    if request.method == "POST":
        form = LessonForm(request.POST)

        # use get_or_create method that ensure the lesson is created before rendering the page
        if form.is_valid():
            lesson, created = Lesson.objects.get_or_create(
                title=form.cleaned_data["title"],
                defaults={
                    "author": request.user,
                    "slug": slugify(form.cleaned_data["title"]),
                    "content": form.cleaned_data["content"],
                    "status": form.cleaned_data["status"],
                },
            )
            if created:
                messages.success(request, "Lesson created successfully.")
            else:
                messages.info(request, "Lesson already exists.")
            return HttpResponseRedirect(reverse("lesson_detail", args=[lesson.slug]))

    form = LessonForm()
    if request.user.is_authenticated:
        return render(request, "lesson/lesson_create.html", {"form": form})
    else:
        messages.add_message(
            request,
            messages.INFO,
            "You are not login, please login or signup.",
        )
        return render(
            request,
            "lesson/index.html",
        )


def lesson_delete(request, slug):
    """
    view to delete a lesson
    """
    lesson = get_object_or_404(Lesson, slug=slug)

    lesson.delete()
    messages.success(request, "Lesson deleted successfully.")
    return redirect("home")


# use the way lesson_create to create a question by parse QuestionForm and question_create.html, also ensure only the author can create Test type questions
def question_create(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    if request.method == "POST":
        question_form = QuestionForm(request.POST, user=request.user, lesson=lesson)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.lesson = lesson
            question.owner = request.user
            question.save()
            messages.success(request, "Question created successfully.")
            return redirect("lesson_detail", slug=lesson.slug)
    else:
        question_form = QuestionForm(user=request.user, lesson=lesson)

    return render(
        request,
        "lesson/question_create.html",
        {"question_form": question_form, "lesson": lesson},
    )
