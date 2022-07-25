from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from item.models import BuyProductModel, ProductModel
from user.models import UserCartModel
from user.form import CartForm




# Create your views here.

def index(request):
    return render(request,'user/index.html')

def about(request):
    return render(request,'user/about.html')

def contact(request):
    return render(request,'user/contactUs.html')

def login(request):
    return render(request,'user/login_register/login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']    
        
        user = authenticate(request,username=username, password=password)

        if user is not None:
            if user.is_superuser == 0:

                log(request,user)
                return redirect('/home')

            else:
                return redirect("/user/login")


        else:
            return redirect("/user/login")

    else:
            return redirect("/user/login")


def register(request):
    return render(request,'user/login_register/register.html')

# To register User

def register_user(request):
    if request.method == "POST":
        User.objects.create_user(
            first_name = request.POST['fullname'],
            username = request.POST['username'],
            password = request.POST['password'],
            email = request.POST['phonenumber'],

        )
        return redirect('/user/login')
    


    else:
        return render(request, '404.html', status=404)

def log_out(request):
    logout(request)
    return redirect('/home')


def shop(request):
    print(request)
    product= ProductModel.objects.all()
    return render(request,'user/shop.html',{'product' : product})

@login_required(login_url='/admin')

def addtocart(request,id,uid):
    data =  UserCartModel(product_id_id=id, user_if_id=uid )
    data.save()

    cart = UserCartModel.objects.filter(user_if_id=id)
    url_id = "/user/cart/%s"%(uid)


    return redirect(url_id)

@login_required(login_url='/user/login')

def  buynow(request,id,uid):
    data =  BuyProductModel(product_id_id=id, user_id_id=uid )
    data.save()

    url_id = "/user/cart/%s"%(uid)
    return redirect(url_id)


@login_required(login_url='/user/login')

def cart(request,id):

    cart = UserCartModel.objects.filter(user_if_id=id)
    item = ProductModel.objects.all()

    buy = BuyProductModel.objects.filter(user_id_id=id)

    return render(request,'user/cart.html',{'cart':cart,'item':item,'buy':buy})

@login_required(login_url='/user/login')

def delete_cart(request,id,uid):
        data = UserCartModel.objects.filter(product_id_id=id,user_if_id=uid)
        data.delete()

        cart = UserCartModel.objects.filter(user_if_id=id)
        item = ProductModel.objects.all()

        url_id = "/user/cart/%s"%(uid)
        return redirect(url_id)



