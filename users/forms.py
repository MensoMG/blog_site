from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User, Author


class NewUserForm(UserCreationForm):
    ...


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('posts',)
