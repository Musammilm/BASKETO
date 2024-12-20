from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import items


def register(request):
 
    if request.method== "POST":
        fname = request.POST["fname"]
        sname = request.POST["sname"]
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["pname"]
        repassword = request.POST["rpname"]

        ucheck =User.objects.filter(username=username)
        echeck = User.objects.filter(email=email)

        if ucheck:
            msg = "Username Exists"
            return render(request,"register.html",{"msg":msg})
        elif echeck:
            msg = "Email EXists"
            return render(request,"register.html",{"msg":msg})
        
        elif password == "" or password !=repassword:
            msg = "Invalid password"
            return render(request,"register.html",{"msg":msg})
        
        else:
            user = User.objects.create_user(
                first_name=fname,last_name=sname,username=username,email=email,password=password)
            user.save()
            return redirect("loginpage")
        
    else:
        return render(request,"register.html")

def login(request):
     if request.method  == "POST":
         username = request.POST["uname"]
         password = request.POST["pass"]

         check = auth.authenticate(username=username,password=password)

         if check is not None:
             auth.login(request,check)
             return redirect("/")
         
         else:
             msg = "Invalid user&pass"
             return render(request,"login.html",{"msg":msg})
     else:
            return render(request,"login.html")
         
def index(request):
     data = items.objects.all()
     return render (request,"index.html",{"pro":data})


def logout(request):
    auth.logout(request)
    return redirect("/")
    
def product(request):
     product = request.GET["id"]
     if request.method == "POST":
        data = items.objects.filter(id=product)
     return render(request,"product.html",{"pro":data})





    

def cart_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('broid')
        quantity = request.POST.get('quantity')
    
        data = items.objects.get(id=product_id)
        total = int(quantity) * int(data.price)
        return render(request, "cart.html", {"pro": data, "total": total,"quantity":quantity})
    else: 
        return render(request, "cart.html")
       


       

def finals(request):
    if request.method == 'POST':
        product_id = request.GET.get('id')
        print(product_id)
        Data =items.objects.filter(id=product_id)
        total = request.GET.get('total')
        quantity = request.GET.get('quantity')
        print(total)
    return render(request,"final.html",{"pro": Data, "total": total,"quantity":quantity})