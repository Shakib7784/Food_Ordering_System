from django.db import models

# Create your models here.

class productList(models.Model):
    choice_category =(
        ("Fast_Food","Fast_Food"),
        ("Chicken_Item","Chicken_Item"),
        ("Beef_Item","Beef_Item"),
        ("Fish_Item","Fish_Item"),

    )
    quantity_type_choice =(
        ("piece","piece"),
        ("plate","plate")
    )
    name = models.CharField(blank=True,max_length=100)
    description = models.CharField(blank=True,max_length=300)
    image = models.ImageField(upload_to="product/")
    price = models.FloatField(blank=True,max_length=50)
    quantity = models.IntegerField(blank=True,null=True)
    quantity_Type = models.CharField(max_length=100,choices=quantity_type_choice,blank=True,default="piece")
    category = models.CharField(max_length=100, choices=choice_category,blank=True,null=True)
    is_approve = models.BooleanField(default=False)
    date_added = models.DateTimeField(blank=True, null = True, auto_now_add=True)


    def __str__(self):
        return self.name


class slider (models.Model):
    title = models.CharField(blank=True, null=True,max_length=200)
    image = models.ImageField(upload_to='slider/')
    # date_added = models.DateTimeField(auto_new_add=True)



    