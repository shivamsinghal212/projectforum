from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
    label='Description',
    widget = forms.Textarea(attrs = {'rows':5, 'placeholder':'Enter a description'}),
    max_length = 4000,
    help_text = 'The max length is 4000 characters')
    class Meta:
        model = Topic
        fields = ['subject','message']
