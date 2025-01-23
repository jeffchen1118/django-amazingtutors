from django import forms
from django.forms import Textarea
from django_summernote.widgets import SummernoteWidget

from .models import Lesson, Note


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
