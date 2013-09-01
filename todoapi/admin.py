from django.contrib import admin
from django.utils.html import format_html

from todoapi.models import Priority, Todo

admin.site.register(Priority)

class TodoAdmin(admin.ModelAdmin):
    list_display = 'formattedTitle', 'dueTo', 'priority',

    def formattedTitle(self, todo):
        if todo.completed:
            return format_html('<del>' + todo.title + '</del>')
        return todo.title
    formattedTitle.short_description = 'title'

admin.site.register(Todo, TodoAdmin)

