from django.db import models

NULLABLE = {'null': True,'blank': True}


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='наименование категории')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(verbose_name='наименование', max_length=100)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(verbose_name='изображение', upload_to='img/', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена', **NULLABLE)
    date_create = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    date_last_change = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
