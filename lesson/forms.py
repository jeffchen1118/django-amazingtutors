from django import forms
from django.forms import Textarea
from django_summernote.widgets import SummernoteWidget

from .models import QUESTIONTYPES, Answer, GradeFeedback, Lesson, Note, Question


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "excerpt", "content", "status"]
        widgets = {
            "content": SummernoteWidget(
                attrs={"summernote": {"height": 300, "width": 400}}
            ),
            "excerpt": Textarea(attrs={"rows": 4, "cols": 30}),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["body"]
        widgets = {
            "body": SummernoteWidget(
                attrs={"summernote": {"height": 300, "width": 400}}
            ),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["body", "preset_answer", "questiontype", "due_date"]  # Always include due_date
        widgets = {
            "body": Textarea(attrs={"rows": 4, "cols": 30}),
            "preset_answer": Textarea(attrs={"rows": 4, "cols": 30}),
            "due_date": forms.DateTimeInput(
                attrs={"type": "datetime-local", "placeholder": "YYYY-MM-DD HH:MM"}
            ),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.lesson = kwargs.pop("lesson", None)
        super().__init__(*args, **kwargs)
        if self.user != self.lesson.author:
            self.fields.pop("due_date")  # Remove due_date for non-authors
            self.fields["questiontype"].choices = [
                choice for choice in QUESTIONTYPES if choice[0] == 0
            ]

    def clean_questiontype(self):
        questiontype = self.cleaned_data.get("questiontype")
        if self.user != self.lesson.author and questiontype == 1:
            raise forms.ValidationError(
                "Only the author can create Test type questions."
            )
        return questiontype


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["body"]
        widgets = {
            "body": Textarea(attrs={"rows": 4, "cols": 30}),
        }


class GradeFeedbackForm(forms.ModelForm):
    class Meta:
        model = GradeFeedback
        fields = ["grade", "feedback"]
        widgets = {
            "body": SummernoteWidget(
                attrs={"summernote": {"height": 300, "width": 400}}
            ),
        }
