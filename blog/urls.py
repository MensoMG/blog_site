from django.urls.conf import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
