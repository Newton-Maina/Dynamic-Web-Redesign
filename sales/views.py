from django.shortcuts import render

# Create your views here.


def index(request):
     return render(request, 'index.html', {'navbar':'index'})


def contact(request):
    return render(request, 'contact.html', {'navbar':'contact'})


def checkout(request):
    return render(request, 'checkout.html',{'navbar':'checkout'})


def blog(request):
    return render(request, 'blog.html',{'navbar':'blog'})


def about(request):
    return render(request, 'about.html', {'navbar':'about'})


def services(request):
    return render(request, 'services.html',{'navbar':'services'})


def shop(request):
    return render(request, 'shop.html',{'navbar':'shop'})

def cart(request):
    return render(request, 'cart.html',{'navbar':'cart'})

def thankyou(request):
    return render(request, 'thankyou.html',{'navbar':'thankyou'})


