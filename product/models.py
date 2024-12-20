from django.db import models


class items(models.Model):
    name = models.CharField(max_length=100)
    image= models.ImageField(upload_to="pic")
    price = models.IntegerField(max_length=100)
    description = models.CharField(max_length=100)

class cart(models.Model):
    product = models.ForeignKey(items, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=100)




# Create your models here.
