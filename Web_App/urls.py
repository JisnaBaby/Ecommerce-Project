from django.urls import path
from Web_App import views
urlpatterns=[
    path('Home/',views.homepage,name="Home"),
    path('About/',views.about_us,name="About"),
    path('Contact/',views.contact_us,name="Contact"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('Products/',views.our_products,name="Products"),
    path('Categories/<cat_name>/',views.filtered_products,name="Categories"),
    path('single_pro/<int:p_id>/',views.single_pro,name="single_pro"),
    path('user_registration/',views.user_registration,name="user_registration"),
    path('',views.user_login,name="user_login"),
    path('save_registration/',views.save_registration,name="save_registration"),
    path('userlogin_/',views.userlogin_,name="userlogin_"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('cart/',views.cart,name="cart"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('delete_cart/<int:ca_id>/',views.delete_cart,name="delete_cart"),
    path('checkoutpage/',views.checkoutpage,name="checkoutpage"),
    path('save_checkout/',views.save_checkout,name="save_checkout"),
    path('pay/',views.pay,name="pay"),
]
