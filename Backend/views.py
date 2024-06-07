from django.shortcuts import render,redirect
from Backend.models import CategoryDb,ProductDb
from WebApp.models import ContactDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def index_page(request):
    return render(request,"index.html")

def Add_category(request):
    return render(request,"Add Category.html")
def display_category_page(request):
    return render(request,"Display_Category.html")
def savedata_Category(request):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('description')
        img = request.FILES['cg_image']
        obj = CategoryDb(Name=na,Description=des,Category_Image=img)
        obj.save()
        return redirect(Add_category)

def display_category(request):
    data = CategoryDb.objects.all()
    return render(request,"Display_Category.html",{'data':data})

def edit_category(request,Categoryid):
    data = CategoryDb.objects.get(id=Categoryid)
    return render(request,"Edit_Category.html", {'data':data})

def update_category(request,Categoryid):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('description')
        try:
            img = request.FILES['cg_image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=Categoryid).Category_Image
        CategoryDb.objects.filter(id=Categoryid).update(Name=na,Description=des,Category_Image=file)
        return redirect(display_category)

def delete_category(request,Categoryid):
    x = CategoryDb.objects.filter(id=Categoryid)
    x.delete()
    return redirect(display_category)

def login_page(request):
    return render(request,"Login.html")

def login_admin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)

            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(index_page)

            else:
                return redirect(login_page)
        else:
            return redirect(login_page)

def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)


# **********************************************************

def Product_page(request):
    cat = CategoryDb.objects.all()
    return render(request,"Products.html",{'cat':cat})

def savedata_Product(request):
    if request.method == "POST":
        s_cat = request.POST.get('sel_category')
        p_na = request.POST.get('name')
        pr = request.POST.get('price')
        des = request.POST.get('description')
        img = request.FILES['pr_image']
        obj = ProductDb(Select_Category=s_cat,Product_Name=p_na,Price=pr,Description=des,Product_Image=img)
        obj.save()
        return redirect(Product_page)

def display_Product(request):
    data = ProductDb.objects.all()
    return render(request,"Display_Products.html",{'data':data})

def edit_product(request,productid):
    data = ProductDb.objects.get(id=productid)
    cat = CategoryDb.objects.all()
    return render(request,"Edit_Product.html", {'data':data, 'cat':cat})

def update_product(request,productid):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('description')
        pr = request.POST.get('price')
        try:
            img = request.FILES['pr_image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=productid).Product_Image
        ProductDb.objects.filter(id=productid).update(Product_Name=na,Description=des,Price=pr,Product_Image=file)
        return redirect(display_Product)

# *****************************************************************************

def Contact_Details(request):
    data = ContactDb.objects.all()
    return render(request,"ContactData.html",{'data':data})

def delete_contact(request,Contactid):
    x = ContactDb.objects.filter(id=Contactid)
    x.delete()
    return redirect(Contact_Details)
