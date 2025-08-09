from django.contrib import admin

from books_app.models import Author, Book, BookReport, AuthorLog


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher_year',)

    readonly_fields = ['size']


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Author, AuthorAdmin)


class BookReportAdmin(admin.ModelAdmin):
    list_display = ('description',)


admin.site.register(BookReport, BookReportAdmin)


class AuthorLogAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(AuthorLog, AuthorLogAdmin)
