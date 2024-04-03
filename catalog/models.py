from django.db import models
from users.models import User


NULLABLE = {'blank': True, 'null': True}


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
    image = models.ImageField(upload_to="product_photo", verbose_name="фото", **NULLABLE)
    category = models.ForeignKey('Category', related_name='products', verbose_name="Категория", on_delete=models.SET_NULL, **NULLABLE)
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.IntegerField(max_length=50, verbose_name="Дата создания (записи в БД)", **NULLABLE)
    updated_at = models.IntegerField(max_length=50, verbose_name="Дата последнего изменения (записи в БД)", **NULLABLE)
    manufactured_at = models.IntegerField(max_length=100, verbose_name="Дата производства продукта", **NULLABLE)
    view_counter = models.PositiveIntegerField(verbose_name="Счетчик Проcмотров", help_text="Укажите кол-во просмотров", default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец", **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name

    permissions = [
        ("change_published", "отменять публикацию продукта",),
        ("change_description", "может менять описание любого продукта",),
        ("change_category", "может менять категорию любого продукта",)
    ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name="Product")
    number = models.IntegerField(verbose_name='номер версии')
    nomination = models.CharField(max_length=50, verbose_name='название')
    is_current = models.BooleanField(default=True, verbose_name='текущая')

    def __str__(self):
        return f'{self.number} ({self.nomination})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('product', 'number', 'nomination', 'is_current')

