from django.contrib import admin
from .models import *
# Register your models here.


class NameeNegariAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'priority', 'receiver', 'created')


admin.site.register(NameeNegari, NameeNegariAdmin)