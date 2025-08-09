from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publisher_year = models.IntegerField()
    pages = models.IntegerField(default=0)
    size = models.CharField(max_length=3)


class BookReport(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AuthorLog(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
