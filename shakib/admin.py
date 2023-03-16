from django.contrib import admin
from shakib.models import slider,productList
# Register your models here.
class productslider(admin.ModelAdmin):
    li = ["title","image"]

class p (admin.ModelAdmin):
    l =['name','image','price']

admin.site.register(slider, productslider)
admin.site.register(productList,p)