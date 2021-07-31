from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])


class Product(models.Model):
    category    = models.ForeignKey(Category, related_name = 'products', on_delete=models.CASCADE)
    name        = models.CharField(max_length=255)
    slug        = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    image       = models.ImageField(upload_to='images/products/%Y/%m/%d', blank=False)
    image_p     = models.ImageField(upload_to='images/products/%Y/%m/%d', blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=0)
    stock       = models.PositiveIntegerField()
    available   = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Наклейка'
        verbose_name_plural = 'Наклейки'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])