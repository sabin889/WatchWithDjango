import imp
import re
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout

from item.models import BuyProductModel, ProductModel
from adminapp.form import MessageForm
from adminapp.models import MessageModel



# Create your views here.


def login(request):
    return render(request,'admin/login/login.html')

@login_required(login_url='/admin')
def index(request):
    return render(request,'admin/index.html')

@login_required(login_url='/admin')
def item(request):
    return render(request,'admin/additem.html')

@login_required(login_url='/admin')
def viewitem(request):
    product= ProductModel.objects.all()
    return render(request,'admin/item.html',{'product' : product})

@login_required(login_url='/admin')
def message(request):
    message = MessageModel.objects.all()
    return render(request,'admin/message.html',{'message':message})


def getmessage(request):
    data = MessageForm(request.POST)
    data.save()

    return redirect('/contact') 

def login_superuser(request):

        username= request.POST['username']
        password= request.POST['password']

        user = authenticate(request,username=username, password=password)

        
        if user is not None:
            log(request,user)

            if user.is_superuser == 1:
                print('here')

                return redirect('/admin/home')

            else:
                return redirect('/admin')

        else:
            return redirect('/admin')
    
def log_out(request):
    logout(request)
    return redirect('/admin')

@login_required(login_url='/admin')

def cart(request):

    buy = BuyProductModel.objects.all()
    item = ProductModel.objects.all()
    user = User.objects.all()
    return render(request,'user/cart.html',{'cart':cart,'item':item,'user':user})


def order(request):
    
    order = BuyProductModel.objects.select_related('product_id','user_id')
    product = ProductModel.objects.all()
    user = User.objects.raw('select * from users')


    return render(request,'admin/order.html',{'order':order})