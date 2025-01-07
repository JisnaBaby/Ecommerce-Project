import datetime
from django.shortcuts import render,redirect
from App_Mart.models import categorydb,ProductDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Web_App.models import contactdb,Registerdb
from django.contrib import messages


# Create your views here.
def index(req):
    x=datetime.datetime.now()
    cat=categorydb.objects.count()
    pro=ProductDb.objects.count()
    return render(req,"index.html",{'cat':cat,'pro':pro,'x':x})
def add_category(req):
    return render(req,"Add_category.html")

def display_category(req):
    data=categorydb.objects.all()
    return render(req, "Display_category.html",{'data':data})

def save_category(request):
    if request.method=="POST":
        cn=request.POST.get('category')
        des=request.POST.get('descript')
        ima=request.FILES['img']
        obj=categorydb(Category_Name=cn,Description=des,C_Images=ima)
        obj.save()
        messages.success(request,"Category saved successfully...")
        return redirect(add_category)
def edit_category(req,c_id):
    data=categorydb.objects.get(id=c_id)
    return render(req,"Edit_category.html",{'data':data})
def update_category(req,c_id):
    if req.method=="POST":
        cn=req.POST.get('category')
        des=req.POST.get('descript')
        try:
            ima = req.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(ima.name,ima)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=c_id).C_Images
    categorydb.objects.filter(id=c_id).update(Category_Name=cn,Description=des,C_Images=file)
    messages.success(req, "Category updated successfully...")
    return redirect(display_category)
def delete_category(req,c_id):
    x=categorydb.objects.filter(id=c_id)
    x.delete()
    messages.error(req, "Category Deleted....")
    return redirect(display_category)


def add_product(req):
    cat = categorydb.objects.all()
    return render(req, "Add_product.html", {'cat': cat})

def save_product(req):
    if req.method == "POST":
        ctna = req.POST.get('cname')
        prna = req.POST.get('pr-name')
        pri = req.POST.get('pr-price')
        des = req.POST.get('pr-description')
        qty = req.POST.get('pr-qty')
        prim = req.FILES['pr-image']
        obj = ProductDb(Category_name=ctna, Product_name=prna, Price=pri, Description=des, Quantity=qty, Product_image=prim)
        obj.save()
        messages.success(req, "Product saved successfully...")
        return redirect(add_product)


def display_product(req):
    data = ProductDb.objects.all()
    return render(req, "DisplayProduct.html", {'data': data})


def edit_product(req, pr_id):
    cat = categorydb.objects.all()
    data = ProductDb.objects.get(id=pr_id)

    return render(req, "EditProduct.html", {'cat': cat,'data': data})


def update_product(req, pr_id):
    if req.method == "POST":
        ctna = req.POST.get('cname')
        prna = req.POST.get('pr-name')
        pri = req.POST.get('pr-price')
        des = req.POST.get('pr-description')
        qty = req.POST.get('pr-qty')
        try:
            prim = req.FILES['pr-image']
            fs = FileSystemStorage()
            file = fs.save(prim.name, prim)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=pr_id).Product_image
            ProductDb.objects.filter(id=pr_id).update(Category_name=ctna, Product_name=prna, Price=pri, Description=des, Quantity=qty, Product_image=file)
            messages.success(req, "Product updated successfully...")
        return redirect(display_product)


def delete_product(req, pr_id):
    x = ProductDb.objects.filter(id=pr_id)
    x.delete()
    messages.error(req, "Product Deleted....")
    return redirect(display_product)

def login_(req):
    return render(req,"Admin_Login.html")

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pw=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pw)
            if x is not None:
                login(request, x)
                request.session['username']=un
                request.session['password']=pw
                messages.success(request, "Welcome to EMart Admin Dashboard ...")
                return redirect(index)

            else:
                messages.warning(request, "Invalid Password...")
                return redirect(login_)
        else:
            messages.warning(request, "Invalid Username...")
            return redirect(login_)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_)
def display_contact(req):
    data = contactdb.objects.all()
    return render(req,"Contact_Details.html",{'data':data})
def delete_contact(req, co_id):
    x = contactdb.objects.filter(id=co_id)
    x.delete()
    return redirect(display_contact)
def display_user(req):
    data = Registerdb.objects.all()
    return render(req, "User_Registration.html", {'data': data})
def delete_user(req, pr_id):
    x = Registerdb.objects.filter(id=pr_id)
    x.delete()
    return redirect(display_user)




