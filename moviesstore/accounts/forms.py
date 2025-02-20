from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from .models import CustomUser
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role = "alert">{e}<div>' for e in self]))

# Unused after hardcoding form in
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'security_question', 'security_answer',)
        help_texts = {
            'username' : None,
        }

    CHOICES = [
        ('value1', 'What was your first pet\'s name?'),
        ('value2', 'What is the name of your elementary school?'),
        ('value3', 'What city did your parents meet each other?'),
    ]

    security_question = forms.ChoiceField(choices=CHOICES)
    security_answer = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['username'].widget.attrs.update({'minlength': '6', 'maxlength': '32', 'autocomplete': 'off'})
        self.fields['password1'].label = 'Password'
        self.fields['password1'].widget.attrs.update({'minlength': '8', 'maxlength': '32', 'autocomplete': 'off'})
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].widget.attrs.update({'minlength': '8', 'maxlength': '32', 'autocomplete': 'off'})
        self.fields['security_question'].label = 'Security Question'
        self.fields['security_answer'].label = 'Security Question Answer'
        self.fields['security_answer'].widget.attrs.update({'minlength': '4', 'maxlength': '32', 'autocomplete': 'off'})


        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class' : 'form-control'},
            )

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
