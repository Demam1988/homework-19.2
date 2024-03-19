from django.db import models

NULLABLE = {'blank':True, 'null':True}



class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')# заголовок,
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(**NULLABLE, verbose_name='содержимое') # содержимое, можно не заполнять
    img_preview = models.ImageField(upload_to='blog_photo', **NULLABLE, verbose_name='изображение') # изображение (превью)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='количество просмотров') # дата создания,
    sign_publication = models.BooleanField(default=True) #признак публикации
    number_views = models.IntegerField(**NULLABLE, default=0, verbose_name='просмотры') # просмотры

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title"]

    def __str__(self):
        return self.title



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


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


class Version(models.Model):
    SIGN_CHOICES = (('active', 'Активна'), ('no_active', 'Не активна'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="get_ver", verbose_name='продукт')
    number_ver = models.CharField(max_length=100, verbose_name='номер версии')
    name_ver = models.CharField(max_length=100, verbose_name='название версии')
    sign_ver = models.BooleanField(max_length=50, choices=SIGN_CHOICES, verbose_name='признак версии')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return f'{self.product} - {self.number_ver}/({self.name_ver})'
