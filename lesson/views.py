from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, IntegerField, Value, When
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.text import slugify
from django.views import generic
from django.views.generic.edit import CreateView

from .forms import AnswerForm, GradeFeedbackForm, LessonForm, NoteForm, QuestionForm
from .models import Answer, GradeFeedback, Lesson, Note, Question

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
    lesson = get_object_or_404(Lesson, slug=slug)
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

    for question in questions:
        question.ordered_answers = question.answers.annotate(
            is_author=Case(
                When(owner=lesson.author, then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )
        ).order_by("-is_author", "created_on")

    if request.user.is_authenticated:  # Check if user is authenticated
        user_note = Note.objects.filter(user=request.user, lesson=lesson).first()
    else:
        user_note = None

    if request.method == "POST":
        form = NoteForm(request.POST, instance=user_note)
        if form.is_valid():
            note = form.save(commit=False)
            note.lesson = lesson
            note.body = form.cleaned_data["body"]
            note.user = request.user
            note.save()
            return redirect("lesson_detail", slug=slug)
    else:
        form = NoteForm(instance=user_note)

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


def question_edit(request, slug, id):
    lesson = get_object_or_404(Lesson, slug=slug)
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        question_form = QuestionForm(
            request.POST, instance=question, user=request.user, lesson=lesson
        )
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.lesson = lesson
            question.owner = request.user
            question.save()
            messages.success(request, "Question updated successfully.")
            return redirect("lesson_detail", slug=lesson.slug)
    else:
        question_form = QuestionForm(
            instance=question, user=request.user, lesson=lesson
        )

    return render(
        request,
        "lesson/question_edit.html",
        {"question_form": question_form, "lesson": lesson, "question": question},
    )


def question_delete(request, slug, id):
    question = get_object_or_404(Question, id=id)
    question.delete()
    messages.success(request, "Question deleted successfully.")
    return redirect("lesson_detail", slug=slug)


def answer_create(request, slug, id):
    lesson = get_object_or_404(Lesson, slug=slug)
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.owner = request.user
            answer.save()
            messages.success(request, "Answer created successfully.")
            return redirect("lesson_detail", slug=slug)
    else:
        answer_form = AnswerForm()

    return render(
        request,
        "lesson/answer_create.html",
        {"answer_form": answer_form, "lesson": lesson, "question": question},
    )


def answer_edit(request, slug, id):
    lesson = get_object_or_404(Lesson, slug=slug)
    answer = get_object_or_404(Answer, id=id)
    if request.method == "POST":
        answer_form = AnswerForm(request.POST, instance=answer)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.owner = request.user
            answer.save()
            messages.success(request, "Answer updated successfully.")
            return redirect("lesson_detail", slug=slug)
    else:
        answer_form = AnswerForm(instance=answer)

    return render(
        request,
        "lesson/answer_edit.html",
        {"answer_form": answer_form, "lesson": lesson, "answer": answer},
    )


def answer_delete(request, slug, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    messages.success(request, "Answer deleted successfully.")
    return redirect("lesson_detail", slug=slug)


def grade_feedback(request, slug, id):
    lesson = get_object_or_404(Lesson, slug=slug)
    answer = get_object_or_404(Answer, id=id)
    grade_feedback = GradeFeedback.objects.filter(answer=answer).first()
    if request.method == "POST":
        grade_feedback_form = GradeFeedbackForm(request.POST, instance=grade_feedback)
        if grade_feedback_form.is_valid():
            grade_feedback = grade_feedback_form.save(commit=False)
            grade_feedback.answer = answer
            grade_feedback.owner = request.user
            grade_feedback.save()
            messages.success(request, "Grade and feedback saved successfully.")
            return redirect("lesson_detail", slug=slug)
    else:
        grade_feedback_form = GradeFeedbackForm(instance=grade_feedback)

    return render(
        request,
        "lesson/grade_feedback.html",
        {
            "grade_feedback_form": grade_feedback_form,
            "lesson": lesson,
            "answer": answer,
            "grade_feedback": grade_feedback,
        },
    )
