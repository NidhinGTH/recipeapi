from django.contrib import admin

# Register your models here.
from recipieapp.models import Recipe ,Review
admin.site.register(Recipe)
admin.site.register(Review)