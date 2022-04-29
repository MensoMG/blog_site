from django.urls.conf import path
from blog import views

urlpatterns = [
    path('', views.blog_index),

]
