from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=255, verbose_name="Названия")
    description = models.TextField(verbose_name="Описания ")
    image = models.ImageField(upload_to='collections/', verbose_name="Фото")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        
