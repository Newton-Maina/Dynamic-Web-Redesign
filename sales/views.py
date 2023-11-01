from django.shortcuts import render

# Create your views here.


def index(request):
     return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def checkout(request):
    return render(request, 'checkout.html')


def cart(request):
    return render(request, 'cart.html')


def blog(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def shop(request):
    return render(request, 'shop.html')


def thankyou(request):
    return render(request, 'thankyou.html')