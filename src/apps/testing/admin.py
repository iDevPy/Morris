from django.contrib import admin
from .models import Authorities


@admin.register(Authorities)
class AuthoritiesAdmin(admin.ModelAdmin):
    pass