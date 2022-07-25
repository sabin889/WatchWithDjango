import imp
from django.shortcuts import redirect, render
from item.models import BuyProductModel, ProductModel
from item.form import ProductForm,ProductFormWithoutImage

# Create your views here.


def add(request):
    data = ProductForm(request.POST, request.FILES)
    data.save()

    return redirect('/admin/item') 


def editproduct(request,id):
    value = ProductModel.objects.get(id=id)
    data = ProductFormWithoutImage(request.POST,instance=value)
    data.save()

    return redirect('/admin/item') 

def edit(request,id):
    data = ProductModel.objects.get(id=id)
    print(data)
    return render(request,"admin/additem.html",{"product":data})

    # return redirect('/admin/additem',{'product':data}) 

def delete(request,id):
    data = ProductModel.objects.get(id=id)
    data.delete()
    return redirect('/admin/item') 

def update(request,id):
    data = ProductModel.objects.get(id=id)
    form = ProductForm(request.POST,request.Files,instance=data)

    form.save()

    return redirect('/admin/item') 

def details(request,id):
    data = ProductModel.objects.get(id=id)

    return render(request,'user/details.html',{'data':data})

def delete_buy(request,id,uid):
        data = BuyProductModel.objects.get(product_id=id,user_id=uid)
        data.delete()

        order = BuyProductModel.objects.select_related('product_id','user_id')
        
        return render(request,'admin/order.html',{'order':order})
