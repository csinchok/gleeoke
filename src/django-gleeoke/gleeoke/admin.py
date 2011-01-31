from gleeoke.models import *
from django.contrib import admin
from django import forms

class VoteAdmin(admin.ModelAdmin):
    list_display = ('badsong', 'worsesong')
    search_fields = ('badsong','worsesong')

admin.site.register(Vote, VoteAdmin)
admin.site.register(Song)
