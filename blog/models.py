from django.db import models
from django.contrib.auth import get_user_model

STATUS = (
    (1, 'Draft'),
    (0, 'Publish')
)


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=50, unique=True, verbose_name='article title')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
