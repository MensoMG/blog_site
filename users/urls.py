from django.urls.conf import path
from .views import profile_page_view


app_name = 'users'
urlpatterns = [
    path('<str:username>/', profile_page_view, name='profile'),
]
