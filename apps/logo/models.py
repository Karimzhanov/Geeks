from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brands/logos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
