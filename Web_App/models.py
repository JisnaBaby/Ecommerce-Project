from django.db import models

# Create your models here.
class contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=200,null=True,blank=True)
    Subject=models.CharField(max_length=200,null=True,blank=True)
    Message=models.CharField(max_length=200,null=True,blank=True)

class Registerdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    C_Password=models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    UserName = models.CharField(max_length=100,null=True,blank=True)
    ProductName = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)
    Prod_Image = models.ImageField(upload_to="Cart images", null=True, blank=True)

class OrderDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=200,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=500,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    Pin = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=500,null=True,blank=True)