from django.urls.conf import path

from .views import profile_page_view, UserLoginView, UserCreateView

app_name = 'users'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('<str:username>/', profile_page_view, name='profile'),
]
