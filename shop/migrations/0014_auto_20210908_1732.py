# Generated by Django 3.2.4 on 2021-09-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20210908_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_p',
            field=models.ImageField(blank=True, upload_to='images/products/%Y/%m/%d'),
        ),
    ]
