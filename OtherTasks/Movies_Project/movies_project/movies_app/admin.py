from django.contrib import admin

from movies_app.models import Movie, Review


# Register your models here.

# StackedInline -> vertical display
# TabularInline -> horizontal display
class ReviewAdminInline(admin.TabularInline):
    model = Review
    extra = 1
    list_display = ('movie', 'comment', 'created_at',)


class MovieAdmin(admin.ModelAdmin):
    inlines = [ReviewAdminInline]
    list_filter = ('genre',)
    search_fields = ('title', 'genre',)
    list_display = ('title', 'description', 'genre', 'average_rating',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
