# Generated by Django 5.0.2 on 2024-03-15 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_product_view_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_ver', models.CharField(max_length=100, verbose_name='номер версии')),
                ('name_ver', models.CharField(max_length=100, verbose_name='название версии')),
                ('sign_ver', models.CharField(choices=[('active', 'Активна'), ('no_active', 'Не активна')], max_length=50, verbose_name='признак версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_ver', to='users.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
