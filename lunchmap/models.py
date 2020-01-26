from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lunchmap:detail', kwargs={'pk': self.pk})
    
class Customer(models.Model):
    name = models.CharField('名前', max_length=20)
    address = models.CharField('住所', max_length=50)
    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('経度', max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = '顧客'
        
    
    