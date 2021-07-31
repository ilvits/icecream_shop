# Generated by Django 3.2.5 on 2021-07-31 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_p',
            field=models.ImageField(blank=True, upload_to='images/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/products/%Y/%m/%d'),
        ),
    ]
