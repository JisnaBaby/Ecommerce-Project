from django.db import models

# Create your models here.
class categorydb(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    C_Images=models.ImageField(upload_to="Category Images",null=True,blank=True)

class ProductDb(models.Model):
    Category_name = models.CharField(max_length=100, null=True, blank=True)
    Product_name = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Product_image = models.ImageField(upload_to="Product images", null=True, blank=True)