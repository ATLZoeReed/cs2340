from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django import forms
from .models import CustomUser




class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role = "alert">{e}<div>' for e in self]))

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'security_question', 'security_question_answer',)

    CHOICES = [
        ('value1', 'What was your first pet\'s name?'),
        ('value2', 'What is the name of your elementary school?'),
        ('value3', 'What city did your parents meet each other?'),
    ]

    security_question = forms.ChoiceField(choices=CHOICES)
    security_question_answer = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )

