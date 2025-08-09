from django.contrib import admin

from books_app.models import Author, Book


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher_year',)


admin.site.register(Book, BookAdmin)
