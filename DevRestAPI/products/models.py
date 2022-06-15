from django.db import models

# Create your models here.

class ProductModel(models.Model):
	id = models.IntegerField(auto_created=True, primary_key=True)
	title = models.CharField(max_length=20)
	category = models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=15, decimal_places=10, default=99.99)


