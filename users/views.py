from django.shortcuts import render
from django.views.generic import DetailView, View

from .models import Author


def profile_page_view(request, username):
    user = Author.objects.get(user__username=username)
    return render(request, template_name='users/profile.html', context={'author': user})

