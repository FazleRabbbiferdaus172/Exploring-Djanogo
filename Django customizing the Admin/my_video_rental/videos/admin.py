from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . import models
# Register your models here.


class MovieAdmin(admin.ModelAdmin):

    fields = ['release_year', 'title', 'length']

    search_fields = ['title']

    list_filter = ['release_year', 'length']

    list_display = ['release_year', 'title', 'length']

    list_editable = ['title', 'length', ]


admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)
