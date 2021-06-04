from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
# Создаем модель товара


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)  # названия товаров не должны повторяться
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    #  создаём категорию, к которой будет привязываться товар


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться

    def __str__(self):
        return f'{self.name.title()}'
