from django import forms
from blog.models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'image', 'content', ]


class PostUpdateView(forms.ModelForm):
    pass
