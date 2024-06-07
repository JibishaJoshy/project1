from django.urls import path
from WebApp import views
urlpatterns=[
    path('',views.homepage,name="home"),
    path('About/',views.Aboutpage,name="About"),
    path('Contact/',views.Contactpage,name="Contact"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('Shop_page/', views.Shop_page, name="Shop_page"),
    path('Filtered_products/<categ_name>/', views.Filtered_products, name="Filtered_products"),
    path('Single_productpage/<int:Pro_id>/', views.Single_productpage, name="Single_productpage"),
    path('Registration_page/', views.Registration_page, name="Registration_page"),
    path('save_Register/', views.save_Register, name="save_Register"),
    path('UserLogin/', views.UserLogin, name="UserLogin"),
    path('UserLogout/', views.UserLogout, name="UserLogout"),
    path('save_Cart/', views.save_Cart, name="save_Cart"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('delete_item/<int:p_id>/', views.delete_item, name="delete_item"),
]