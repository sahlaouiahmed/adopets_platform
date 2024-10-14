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
    city = models.CharField(max_length=100, default='Default City')  # Adding default value
    country = models.CharField(max_length=100, default='Default Country')  # Adding default value
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_pets')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["posted_at"]


class AdoptionRequest(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_requests')
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester.username} - {self.pet.name}"  

    class Meta:
        ordering = ["created_at"]
