from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000, null=True, blank=True)
    icon = models.ImageField(upload_to='images/', default='images/services-icon.png')
    image = models.ImageField(upload_to='images/', default=0)
    products = models.TextField(max_length=1000, default=0)
    price = models.IntegerField(default=0)

    def products_list(self):
        return self.products.split(',')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title