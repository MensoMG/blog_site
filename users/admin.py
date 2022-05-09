from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import User, Author

admin.site.register(User, UserAdmin)
admin.site.register(Author)
