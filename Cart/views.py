from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from Product.models import ProductDetail
from .models import Cart

@login_required(login_url="SignIn")
def CartView(request):
    item= Cart.objects.filter(user=request.user)
    context={
        "product":item  
    }

    return render(request,'cart.html',context)

@login_required(login_url="SignIn")
def AddCart(request,pk):
    product = ProductDetail.objects.get(ProductId = pk)
    cartitem = Cart.objects.create(product = product, numberofitems = 1, user = request.user)
    cartitem.save()
    return redirect('CartView')

def Dele(request,pk):
    product = Cart.objects.get(id = pk)
    product.delete()
    return redirect('CartView')