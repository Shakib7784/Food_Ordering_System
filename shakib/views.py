from django.shortcuts import render
from django.http import HttpResponse
from shakib.models import slider,productList

# Create your views here.
def home(request):
    s = slider.objects.all()
    p = productList.objects.all()[:8]
    dic = {
        "slid":s,
        "pro":p,
    }
    # for i in p:
    #     print(i.id)
    return render(request,"home/home.html",dic)


def single_product(request,pid):
    singleproduct = productList.objects.get(id=pid)
    data ={
        "sproduct":singleproduct,
    }
    

    return render(request,"product_single/single_product.html",data)




