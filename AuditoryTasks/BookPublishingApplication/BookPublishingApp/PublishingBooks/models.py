from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    EMBG = models.CharField(max_length=13)
    year_of_birth = models.IntegerField()
    country = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)

    # representation of objects in the admin panel by their first_name and last_name
    def __str__(self):
        return self.first_name + " " + self.last_name


class Publication(models.Model):
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Book: (1) | Author: (M)
# Book: (1) | Publication: (M)
class Book(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=17)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(null=True, blank=True)


# Publication: (M) | Author: (N)
class PublicationAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True, blank=True)
