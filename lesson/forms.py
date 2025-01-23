from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Lesson, Note


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "content", "status"]
        widgets = {
            "content": SummernoteWidget(
                attrs={"summernote": {"height": 300, "width": 400}}
            ),
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
