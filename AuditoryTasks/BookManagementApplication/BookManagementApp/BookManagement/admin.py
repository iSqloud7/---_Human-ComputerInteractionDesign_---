from django.contrib import admin

from BookManagement.models import Genre, Translator, Book, BookRating, GenreBook, TranslatorBook


# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Genre, GenreAdmin)


class TranslatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')
    list_filter = ('name', 'nationality')


admin.site.register(Translator, TranslatorAdmin)


class BookRatingInline(admin.TabularInline):
    model = BookRating
    fields = ('user', 'rating', 'comment')
    extra = 0


admin.site.register(BookRating)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'owner', 'publication_date', 'isAvailable')
    list_filter = ('isAvailable',)
    search_fields = ('title', 'author')
    inlines = [BookRatingInline]

    readonly_fields = ('owner',)

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj:
            return obj.owner == request.user or request.user.is_superuser
        return False

    def has_delete_permission(self, request, obj=None):
        if obj:
            return obj.owner == request.user
        return False


admin.site.register(Book, BookAdmin)


class GenreBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'genre')


admin.site.register(GenreBook, GenreBookAdmin)


class TranslatorBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'translator')


admin.site.register(TranslatorBook, TranslatorBookAdmin)
