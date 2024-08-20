from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/', null=True, blank=True)  # Optional

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        
