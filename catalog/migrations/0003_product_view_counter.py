# Generated by Django 5.0.2 on 2024-03-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view_counter',
            field=models.PositiveIntegerField(default=0, help_text='Укажите кол-во прсмотров', verbose_name='Счетчик Провмотров'),
        ),
    ]
