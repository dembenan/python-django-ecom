from datetime import timezone
from django.db import models
from django.urls import reverse
from shop.settings import AUTH_USER_MODEL

# Create your models here.

#Model pour les produits
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products",blank=True,null=True)
    
    def __str__(self):                      
        return f"{self.name} ({self.stock} en stock)"
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"id": self.id})
    
    
#Model pour les Commandes
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    #ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    def delete(self,*args,**kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()
            
        self.orders.clear()
        super().delete(*args,**kwargs)
        
        

    
    
