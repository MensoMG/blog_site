from django.shortcuts import render
from django.views import generic

from blog.models import Post


def blog_index(request):
    return render(request, 'blog/base.html', context={})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/base.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
