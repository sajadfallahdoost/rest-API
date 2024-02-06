from django.contrib import admin
from books.models import Book  # Adjust the import path if necessary


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'code', 'stock')  # Customize as needed
    search_fields = ('title', 'author')
    list_filter = ('author',)


# Register your models here.
admin.site.register(Book, BookAdmin)
