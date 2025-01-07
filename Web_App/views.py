from django.shortcuts import render,redirect
from App_Mart.models import categorydb,ProductDb
from Web_App.models import contactdb,Registerdb,CartDb,OrderDb
from django.contrib import messages
import razorpay

# Create your views here.
def homepage(req):
    item=CartDb.objects.filter(UserName=req.session['Username']).count()

    category=categorydb.objects.all()
    return render(req,"Home.html",{'category':category,'cart':cart,'item':item})
def about_us(req):
    item=CartDb.objects.filter(UserName=req.session['Username']).count()

    category = categorydb.objects.all()
    return render(req,"about.html",{'category':category,'item':item})
def contact_us(req):
    item=CartDb.objects.filter(UserName=req.session['Username']).count()

    category = categorydb.objects.all()
    return render(req,"contact.html",{'category':category,'item':item})
def save_contact(req):
    if req.method=="POST":
        nm=req.POST.get('name')
        em=req.POST.get('mail')
        sb=req.POST.get('sub')
        ms=req.POST.get('msg')
        obj=contactdb(Name=nm,Email=em,Subject=sb,Message=ms)
        obj.save()
        return redirect(contact_us)
def our_products(req):
    item=CartDb.objects.filter(UserName=req.session['Username']).count()

    category = categorydb.objects.all()
    pro=ProductDb.objects.all()
    return render(req,"All_Products.html",{'pro':pro,'category':category,'item':item})
def filtered_products(req,cat_name):
    item = CartDb.objects.filter(UserName=req.session['Username']).count()
    category = categorydb.objects.all()
    pro=ProductDb.objects.filter(Category_name=cat_name)
    return render(req,"Filtered_products.html",{'pro':pro,'category':category,'item':item})
def single_pro(req,p_id):
    item=CartDb.objects.filter(UserName=req.session['Username']).count()

    category = categorydb.objects.all()
    data=ProductDb.objects.get(id=p_id)
    return render(req,"Single_Product.html",{'data':data,'category':category,'item':item})

def user_registration(request):
    return render(request,"user_register.html")

def user_login(request):
    return render(request,"User_Login.html")
def save_registration(req):
    if req.method=="POST":
        user=req.POST.get('uname')
        em=req.POST.get('mail')
        phn=req.POST.get('mob')
        pwd=req.POST.get('pass')
        cpwd=req.POST.get('c_pass')
        obj=Registerdb(Username=user,Email=em,Mobile=phn,Password=pwd,C_Password=cpwd)
        obj.save()
        messages.success(req,"Registered to E Mart Successfully......")
        return redirect(user_registration)
def userlogin_(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pw=request.POST.get('upwd')
        if Registerdb.objects.filter(Username=un,Password=pw).exists():
            request.session['Username']=un
            request.session['Password']=pw
            messages.success(request,"Welcome to E Mart")
            return redirect(homepage)
        else:
            messages.warning(request,"Invalid Username or Password....")
            return redirect(user_login)
    else:
        messages.warning(request, "Invalid Username or Password....")
        return redirect(user_login)
def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logout successfully")
    return redirect(user_login)

def cart(request):
    item=CartDb.objects.filter(UserName=request.session['Username']).count()


    sub_total = 0
    shipping_charge = 0
    total = 0
    data=CartDb.objects.filter(UserName=request.session['Username'])
    category = categorydb.objects.all()
    for i in data:
        sub_total += i.TotalPrice
        if sub_total>1000:
            shipping_charge = 20
        else:
            shipping_charge = 40
        total = shipping_charge + sub_total

    return render(request,"Cart.html",{'data':data,'category':category,'sub_total':sub_total,
                                       'shipping_charge':shipping_charge,'total':total,'item':item})

def save_cart(req):
    if req.method=="POST":
        pr=req.POST.get('rs')
        tpr=req.POST.get('trs')
        usr=req.POST.get('user')
        pro=req.POST.get('proname')
        qu=req.POST.get('quantity')
        try:
            x = ProductDb.objects.get(Product_name=pro)
            img = x.Product_image
        except ProductDb.DoesNotExist:
            img = None

        obj=CartDb(UserName=usr, ProductName=pro, Quantity=qu,Price=pr, TotalPrice=tpr, Prod_Image=img)
        obj.save()
        return redirect(cart)
def delete_cart(req,ca_id):
    x = CartDb.objects.filter(id=ca_id)
    x.delete()
    return redirect(cart)

def checkoutpage(request):
    item=CartDb.objects.filter(UserName=request.session['Username']).count()

    sub_total = 0
    shipping_charge = 0
    total = 0
    data = CartDb.objects.filter(UserName=request.session['Username'])
    category = categorydb.objects.all()
    for i in data:
        sub_total += i.TotalPrice
        if sub_total > 1000:
            shipping_charge = 20
        else:
            shipping_charge = 40
        total = shipping_charge + sub_total
    return render(request,"checkout.html",{'data': data,'category': category,'sub_total': sub_total,
                                       'shipping_charge': shipping_charge,'total': total,'item':item})

def save_checkout(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        em=request.POST.get('mail')
        pl=request.POST.get('loc')
        ad=request.POST.get('add')
        phn=request.POST.get('mob')
        st=request.POST.get('state')
        zip=request.POST.get('pin')
        pr=request.POST.get('tot')
        ch=request.POST.get('msg')
        obj=OrderDb(Name=nm,Email=em,Place=pl,Address=ad,Mobile=phn,State=st,Pin=zip,Total_Price=pr,Message=ch)
        obj.save()
        return redirect(pay)
def pay(request):
    customer = OrderDb.objects.order_by('-id').first()
    pay=customer.Total_Price
    amount = int(pay*100)
    pay_str = str(amount)
    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_v5JbppqXvm3HVl','ttWboR6lZrmOVlN2ZQnrZy7w'))
        payment = client.order.create({'amount':amount,'currency':order_currency})
    return render(request,"Payment.html",{'customer':customer,'pay_str':pay_str})
