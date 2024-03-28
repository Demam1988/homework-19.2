from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {
    'blank': True,
    'null': True,
}


class User(AbstractUser):

    username = None

    email = models.EmailField(max_length=60, help_text="Ведите email", unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/avatar',
                               verbose_name='аватар', help_text="Загрузите изображение", **NULLABLE)
    phone_number = models.CharField(max_length=35,
                                    verbose_name="номер телефона", help_text="Укажите номер телеыона", **NULLABLE)
    country = models.CharField(max_length=255,
                               verbose_name="страна", help_text="Укажите страну", **NULLABLE)
    token = models.CharField(max_length=50, verbose_name='Токен', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


