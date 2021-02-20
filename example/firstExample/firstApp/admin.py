#!/usr/bin/env python3

from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Movies)


# Customize admin page  publisher table display
class DisplayPublisher(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'city', 'state_province', 'country')
    search_fields = ['id', 'name', 'address', 'city', 'state_province', 'country']
    list_filter = ('id', 'name', 'address', 'city', 'state_province', 'country')

admin.site.register(Publisher, DisplayPublisher)
