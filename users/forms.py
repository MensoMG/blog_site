from django import forms
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _

from users.models import User, Author


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('posts',)


class UserLoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,
                                                           "class": "shadow appearance-none border rounded w-full "
                                                                    "py-2 px-3 text-gray-700 leading-tight "
                                                                    "focus:outline-none focus:shadow-outline",
                                                           "name": "username",
                                                           "placeholder": "username"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "class": "shadow appearance-none border rounded w-full py-2 px-3 "
                                                   "text-gray-700 mb-3 leading-tight focus:outline-none "
                                                   "focus:shadow-outline",
                                          "type": "password",
                                          "placeholder": "password",
                                          "name": "password",
                                          }),
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "username" field.
        self.username_field = User._meta.get_field(User.USERNAME_FIELD)
        username_max_length = self.username_field.max_length or 254
        self.fields["username"].max_length = username_max_length
        self.fields["username"].widget.attrs["maxlength"] = username_max_length
        if self.fields["username"].label is None:
            self.fields["username"].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"username": self.username_field.verbose_name},
        )


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', )

    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,
                                                           "class": "shadow appearance-none border rounded w-full "
                                                                    "py-2 px-3 text-gray-700 leading-tight "
                                                                    "focus:outline-none focus:shadow-outline",
                                                           "name": "username",
                                                           }))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "shadow appearance-none border rounded w-full py-2 px-3 "
                                                   "text-gray-700 mb-3 leading-tight focus:outline-none "
                                                   "focus:shadow-outline",
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "shadow appearance-none border rounded w-full py-2 px-3 "
                                                   "text-gray-700 mb-3 leading-tight focus:outline-none "
                                                   "focus:shadow-outline",
                                          }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
