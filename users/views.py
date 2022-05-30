from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import UserLoginForm, UserCreateForm
from .models import Author, User


def profile_page_view(request, username):
    user = Author.objects.get(user__username=username)
    return render(request, template_name='users/profile.html', context={'author': user})


class UserLoginView(LoginView):
    template_name = 'registration/sign_in.html'
    form_class = UserLoginForm


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return

