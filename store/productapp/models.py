from django.db import models

# Create your models here.
class Product(models.Model): #product is inheriting the model
    CAT=((1,'Mobile'),(2,'Shoes'),(3,'clothes'))
    AVAIL=((0,'no'),(1,'yes'))
    name=models.CharField(max_length=50,verbose_name="Product name")
    price=models.FloatField(verbose_name="Price(per qty)")
    qty=models.IntegerField(verbose_name="Quantity")
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    is_vail=models.BooleanField(verbose_name="Is_available",choices=AVAIL)

    def __str__(self):
        return str(self.id)#converting the int into string
    
    
