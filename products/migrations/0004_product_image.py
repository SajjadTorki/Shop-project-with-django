# Generated by Django 5.0 on 2024-01-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_comment_managers_alter_comment_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_cover/', verbose_name='Product Image'),
        ),
    ]