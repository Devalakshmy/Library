from django.contrib import admin
from users.models import CustomUser,Users

admin.site.register(Users)

admin.site.register(CustomUser)