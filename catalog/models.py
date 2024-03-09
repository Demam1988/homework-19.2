from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    category = models.CharField(max_length=100, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(max_length=300, verbose_name="Описание")
    image = models.ImageField(upload_to="product_photo", verbose_name="фото", blank=True, null=True)
    category = models.ForeignKey('Category', related_name='products', verbose_name="Категория", on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.IntegerField(max_length=50, verbose_name="Дата создания (записи в БД)", blank=True, null=True)
    updated_at = models.IntegerField(max_length=50, verbose_name="Дата последнего изменения (записи в БД)", blank=True, null=True)
    manufactured_at = models.IntegerField(max_length=100, verbose_name="Дата производства продукта", blank=True, null=True)


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


