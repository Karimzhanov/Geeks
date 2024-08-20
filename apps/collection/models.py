from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='collections/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        
