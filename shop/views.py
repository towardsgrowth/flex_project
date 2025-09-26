from django.shortcuts import render

def dashboard(request):
    return render(request, "shop/index.html")


def detail(request):
    return render(request, "shop/details.html")
