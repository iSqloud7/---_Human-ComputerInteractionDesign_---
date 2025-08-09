from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Movie(models.Model):
    GENRES_CHOICES = [
        ("Horror", "Horror"),
        ("Romance", "Romance"),
        ("Sci-Fi", "Sci-Fi"),
        ("Fantasy", "Fantasy"),
        ("Animation", "Animation"),
        ("Action", "Action"),
        ("Drama", "Drama"),
        ("Thriller", "Thriller"),
        ("Western", "Western"),
        ("Academic", "Academic"),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRES_CHOICES)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    def update_rating(self):
        reviews = Review.objects.filter(movie=self)

        if reviews.exists():
            self.average_rating = sum(review.rating for review in reviews) / len(reviews)
        else:
            self.average_rating = 0.0

        self.save()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"Movie: {self.movie} ---> Comment: {self.comment} ---> CreatedAt: {self.created_at} ---> Rating: {self.rating}"

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        self.movie.update_rating()
