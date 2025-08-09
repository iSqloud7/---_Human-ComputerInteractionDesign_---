from django.db import models


# Create your models here.
class Supplement(models.Model):
    CATEGORY_CHOICES = [
        ("PR", 'Proteins'),
        ("VI", "Vitamins"),
        ("CR", "Creatines"),
        ("AA", "Amino Acids"),
        ("PW", "Pre-Workout")
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='supplements_images/', blank=True, null=True)
    code = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name