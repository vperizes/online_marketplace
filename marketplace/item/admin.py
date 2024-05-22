from django.contrib import admin
from .models import Categories

# show db table in admin interface
admin.site.register(Categories)
