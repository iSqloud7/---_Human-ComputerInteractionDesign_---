from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Translator(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.nationality}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    # genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    publication_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    numOfPages = models.IntegerField()
    coverImage = models.ImageField(upload_to='Covers/', null=True, blank=True)
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author} owned by {self.owner.username if self.owner else 'Unknown'}!"


class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} rated {self.book.title} with {self.rating}!"


class GenreBook(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} - {self.genre.name}"


class TranslatorBook(models.Model):
    translator = models.ForeignKey(Translator, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def str_(self):
        return f"{self.book.title} translated by {self.translator.name}!"
