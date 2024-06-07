from django.shortcuts import render,redirect
from Backend.models import ProductDb,CategoryDb
from WebApp.models import ContactDb,RegisterDb,CartDb
from django.contrib import messages

# Create your views here.
def homepage(request):
    cat = CategoryDb.objects.all()
    return render(request,"Home.html",{'cat':cat})

def Aboutpage(request):
    cat = CategoryDb.objects.all()
    return render(request,"About.html",{'cat':cat})

def Contactpage(request):
    cat = CategoryDb.objects.all()
    return render(request,"Contact.html",{'cat':cat})

def save_contact(request):
    if request.method== "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        me = request.POST.get('message')
        obj = ContactDb(Name=na, Email=em, Subject=sub,Message=me)
        obj.save()
        return redirect(Contactpage)


def Shop_page(request):
    prod = ProductDb.objects.all()
    cat = CategoryDb.objects.all()
    return render(request,"Shop.html",{'prod':prod,'cat':cat})

def Filtered_products(request,categ_name):
    data = ProductDb.objects.filter(Select_Category=categ_name)
    return render (request,"Products_filtered.html",{'data':data})

def Single_productpage(request,Pro_id):
    data = ProductDb.objects.get(id=Pro_id)
    cat = CategoryDb.objects.all()
    return render(request,"Single_product.html",{'data':data,'cat':cat})

def Registration_page(request):
    return render(request,"Register.html")

def save_Register(request):
    if request.method== "POST":
        na = request.POST.get('username')
        em = request.POST.get('email')
        pas = request.POST.get('pass1')
        obj = RegisterDb(Username =na,Email=em,Password=pas)
        if RegisterDb.objects.filter(Username =na).exists():
            messages.warning(request,"Username already exists...!")
            return redirect(homepage)
        elif RegisterDb.objects.filter(Email=em).exists():
            messages.warning(request,"Email already exists..!")
        else:
            obj.save()
            messages.success(request, "Registered successfully...!")
        return redirect(homepage)

def UserLogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if RegisterDb.objects.filter(Username=un,Password=pswd).exists():
            request.session['Username']=un
            request.session['Password'] = pswd
            return redirect(homepage)

        else:
            return redirect(Registration_page)
    else:
        return redirect(Registration_page)

def UserLogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(homepage)

def save_Cart(request):
    if request.method== "POST":
        na = request.POST.get('username')
        pr = request.POST.get('price')
        qty = request.POST.get('quantity')
        pr_na = request.POST.get('Product_name')
        obj = CartDb(Username=na, Quantity=qty, Price=pr,Productname=pr_na)
        obj.save()
        return redirect(homepage)

def cartpage(request):
    data = CartDb.objects.filter(Username=request.session['Username'])
    total = 0
    for d in data:
        total = total+d.Price
    return render(request,"Cart.html",{'data':data,'total':total})

def delete_item(request,p_id):
    x = CartDb.objects.filter(id=p_id)
    x.delete()
    return redirect(cartpage)
