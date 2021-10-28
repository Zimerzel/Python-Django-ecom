from django.db import models

# Create your models here.
class Category(model.Model):
    name = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(max_length=225, db_index=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
    return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=255, default='admin')
    desciption = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=225)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plurual = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title