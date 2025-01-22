from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["body"]
        widgets = {
            "body": SummernoteWidget(
                attrs={"summernote": {"height": 300, "width": 420}}
            ),
        }
