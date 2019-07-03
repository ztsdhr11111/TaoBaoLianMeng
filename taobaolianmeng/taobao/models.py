from django.db import models
from django.conf import settings

# Create your models here.
class Shop(models.Model):
    name = models.CharField(verbose_name='商品名称', max_length=150)
    price = models.IntegerField(verbose_name='商品价格')

    def __str__(self):
        return self.name


    
