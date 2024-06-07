from django.urls import path
from Backend import views
urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('Add_category',views.Add_category,name="Add_category"),
    path('display_category_page/',views.display_category_page,name="display_category_page"),
    path('savedata_Category', views.savedata_Category, name="savedata_Category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:Categoryid>/',views.edit_category,name="edit_category"),
    path('update_category/<int:Categoryid>/',views.update_category,name="update_category"),
    path('delete_category/<int:Categoryid>/',views.delete_category,name="delete_category"),
    path('login_page/',views.login_page,name="login_page"),
    path('login_admin/',views.login_admin,name="login_admin"),
    path('Adminlogout/',views.Adminlogout,name="Adminlogout"),
    path('Product_page/',views.Product_page,name="Product_page"),
    path('savedata_Product', views.savedata_Product, name="savedata_Product"),
    path('display_Product/',views.display_Product,name="display_Product"),
    path('edit_product/<int:productid>/',views.edit_product,name="edit_product"),
    path('update_product/<int:productid>/',views.update_product,name="update_product"),

    path('Contact_Details/',views.Contact_Details,name="Contact_Details"),
    path('delete_contact/<int:Contactid>/',views.delete_contact,name="delete_contact"),


]