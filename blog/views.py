from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.forms import PostCreateForm
from blog.models import Post


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/forms/post_create.html'
    form_class = PostCreateForm

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse_lazy('blog:post-detail', args=[post.slug]))
        return render(request, 'blog/forms/post_create.html', {'form': form})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/forms/post_edit.html'
    fields = ['title', 'content', ]
    # TODO: исправить ошибку NoReverseMatch при роуте на 'blog:post-detail'
    success_url = reverse_lazy('blog:home', )


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/forms/post_delete.html'
    success_url = reverse_lazy('blog:home')


# --------------------------------------------------------------------- #
class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on').select_related()
    context_object_name = 'post_list'
    paginate_by = 6
    template_name = 'blog/post_list.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
