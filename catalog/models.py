from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='img/', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_modified = models.DateField(auto_now=True, verbose_name='Дата последнего изменения', null=True, blank=True)
    vers = models.ForeignKey('Version', verbose_name='Версия', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f"{self.name}({self.phone})"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Version(models.Model):
    product_version = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE, related_name='versions')
    number_version = models.PositiveIntegerField(verbose_name='Номер версии')
    name_version = models.CharField(max_length=100, verbose_name='Имя версии')
    current_version = models.BooleanField(verbose_name='Текущая версия', default=False)

    def __str__(self):
        return f"{self.product} - {self.name_version}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'