from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='pet_photos/')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_pets')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | Posted by {self.posted_by}"
    class Meta:
        ordering = ["posted_at"]