from django.db import models

class Product(models.Model):
    # id = models.DecimalField(primary_key = True)
    name = models.CharField(max_length = 100)
    price = models.DecimalField(decimal_places = 2, max_digits = 100)
    description = models.TextField(blank = True, null = True) 
    department = models.CharField(max_length = 100, blank = True, null = True)
    img = models.CharField(max_length = 100)
