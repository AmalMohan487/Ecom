from django.shortcuts import render, redirect
from .forms import ProductAddForm
from django.contrib import messages
from .models import ProductDetail
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="SignIn")
def AddProduct(request):
    form = ProductAddForm()
    if request.method == "POST":
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            product =form.save()
            product.Merchant = request.user
            product.save()
            messages.info(request,"Product Added to list")
            return redirect('AddProduct')
    return render(request,'admin/addproduct.html',{"form":form})

def ProductViewMerchant(request):
    products = ProductDetail.objects.all()
    context ={
        "products":products
    }
    return render(request,'admin/productlistview.html',context)

@login_required(login_url="SignIn")
def DeleteProduct(request,pk):
    product = ProductDetail.objects.get(ProductId =pk)
    product.Product_Image.delete()
    product.delete()
    messages.info(request,"Product Deleted")

    return redirect('ProductViewMerchant')

@login_required(login_url="SignIn")
def UpdateProduct(request,pk):
    product = ProductDetail.objects.filter(ProductId =pk)
    if request.method=="POST":
        pname= request.POST['pname']
        pbrand= request.POST['pbrand']
        pdis= request.POST['pdis']
        pstk= request.POST['pstock']
        pcat= request.POST['pcat']
        pprice= request.POST['pprice']
        img= request.FILES['img']

        item=ProductDetail.objects.get(ProductId = pk)

        item.Product_Name = pname
        item.Product_Brand = pbrand
        item.Product_Discription = pdis
        item.Product_Price = pprice
        item.Product_Category = pcat
        item.Product_Stock = pstk
        item.Product_Image.delete()
        item.Product_Image = img
        item.save()

        messages.info(request,"item updated")


        return redirect("UpdateProduct",pk=pk)
    context={
        "product":product  
    }

    return render(request,'admin/updateproduct.html',context)
    
@login_required(login_url="SignIn")
def prodctlistview(request,pk):
    item = ProductDetail.objects.filter(ProductId=pk)
    context={
        "product":item  
    }

    return render(request,'prodctlistview.html',context)