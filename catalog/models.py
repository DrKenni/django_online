from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    last_change = models.DateField(verbose_name='дата последнего изменения', **NULLABLE)
    date_create = models.DateField(verbose_name='дата создания', auto_now=True)
    price = models.IntegerField(verbose_name='цена')
    preview_image = models.ImageField(verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}({self.category}): {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, **NULLABLE, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=100, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    version_sign = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product} Номер версии:{self.version_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
