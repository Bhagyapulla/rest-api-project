from django.contrib import admin

# Register your models here.
from .models import FormAuthor,FormBook
admin.site .register(FormAuthor)
admin.site .register(FormBook)

