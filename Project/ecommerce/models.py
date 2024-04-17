from django.db import models

# Create your models here.
class Item(models.Model):
    item_name     = models.CharField(max_length=200)
    item_date     = models.DateField(default="2002-02-28")
    item_quantity = models.IntegerField(default=0)

