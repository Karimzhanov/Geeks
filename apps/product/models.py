from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Названия товара ")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара ")
    image = models.ImageField(upload_to='products/', verbose_name="Фото товара ")
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
