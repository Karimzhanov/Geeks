from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='banners/', null=True, blank=True, verbose_name="Изображение")  # Optional

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
