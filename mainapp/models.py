from django.db import models
from django.conf import settings
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # discount = models.IntegerField(default=0, verbose_name='скидка')
    # discount = models.IntegerField(label='скидка', required=False, min_value=0, max_value=90, initial=0)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        if settings.LOW_CACHE:
            key = 'categories'
            categories = cache.get(key)
            if categories is None:
                categories = cls.objects.all()
                cache.set(key, categories)

            return categories
        else:
            return cls.objects.all()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(ProductCategory, self).save()
        cache.delete('categories')

class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} | {self.category.name}'

@receiver(pre_save, sender=ProductCategory)
def product_is_active_update_save_productcategory(sender, instance, **kwargs):
    if instance.pk:
        if instance.is_active:
            instance.product_set.update(is_active=True)
        else:
            instance.product_set.update(is_active=False)
