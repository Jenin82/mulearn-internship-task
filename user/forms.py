from django import forms
from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
  class Meta:
    model = Todo
    fields = '__all__'
    exclude = ['title','description','status','task_time',]
    widgets = {
            'completion_date': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }
