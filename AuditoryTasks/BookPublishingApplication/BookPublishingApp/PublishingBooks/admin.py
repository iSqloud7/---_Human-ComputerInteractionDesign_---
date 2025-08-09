from django.contrib import admin

from .models import Author, Publication, Book, PublicationAuthor


# Register your models here.

# class for how the model will be displayed in the admin panel
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'year_of_birth')
    list_filter = ('first_name', 'year_of_birth')

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication')
    list_filter = ('title',)


admin.site.register(Book, BookAdmin)


class PublicationAuthorAdmin(admin.StackedInline):
    model = PublicationAuthor
    extra = 0
    list_display = ('author', 'publication')


# admin.site.register(PublicationAuthor, PublicationAuthorAdmin)

class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationAuthorAdmin,]
    list_display = ('name', 'city', 'country')
    list_filter = ('name', 'city')


admin.site.register(Publication, PublicationAdmin)
