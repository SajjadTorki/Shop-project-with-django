# Generated by Django 5.0 on 2024-01-13 08:14

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('active_comments_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name=' نظرات'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='star',
            field=models.CharField(choices=[('1', 'خیلی بد'), ('2', 'بد'), ('3', 'عادی'), ('4', 'خوب'), ('5', 'خیلی خوب')], max_length=10, verbose_name='امتیازات شما'),
        ),
    ]
