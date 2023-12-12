from django import forms
from .models import Topic
from .models import Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.TextInput(attrs={"class": "add-topic-input"})}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text", "flag_status", "file"]
        labels = {"text": "", "flag_status": "Change status:", "file": "Add your file:"}
        widgets = {
            "text": forms.Textarea(attrs={"cols": 100, "class": "entry-text-area"}),
            "flag_status": forms.Select(attrs={"class": "select"}),
            "file": forms.FileInput(attrs={"class": "fileInput"})
        }
