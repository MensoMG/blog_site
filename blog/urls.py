from django.urls.conf import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_index, name='home'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
