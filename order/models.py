from django.db import models
from django.db.models.fields import CharField

class MenuCategory(models.Model):
    categoryname=models.CharField(max_length=50)
    
    def __str__(self):
        return self.categoryname
class Menu(models.Model):
    dish=models.CharField(max_length=50)
    ingredient=models.CharField(max_length=150)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    category=models.ForeignKey(MenuCategory,on_delete=models.CASCADE)

