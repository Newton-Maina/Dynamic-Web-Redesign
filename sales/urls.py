from django.urls import path

from . import views


app_name = "sales"
urlpatterns = [
    path('', views.index, name="index"),
path('contact/', views.contact, name="contact"),
   path('checkout/', views.checkout, name="checkout"),
path('cart/', views.cart, name="cart"),
   path('blog/', views.blog, name="blog"),
path('about/', views.about, name="about"),
   path('services/', views.services, name="services"),
path('shop/', views.shop, name="shop"),
   path('thankyou/', views.thankyou, name="thankyou"),

]