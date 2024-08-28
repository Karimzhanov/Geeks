from django.db import models

# Create your models here.

class Logo(models.Model):
    logo = models.ImageField(upload_to='logos/', verbose_name="Логотип")

    def __str__(self):
        return self.logo.url if self.logo else "No logo"

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'
