from django import forms
from .models import Topic
from .models import Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'flag_status']
        labels = {'text': 'Entry:', 'flag_status': 'Change status:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}
        
