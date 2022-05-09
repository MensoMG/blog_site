from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='post-date-(%Y-%m-%d)/',
                              default=f'{settings.BASE_DIR / "media" / "dafault_post.jpg"}', blank=True)
    title = models.CharField(max_length=50, unique=True, verbose_name='article title')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
