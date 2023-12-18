from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    output = models.ImageField(upload_to='outputs/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name