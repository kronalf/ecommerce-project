from django.shortcuts import render

def home(request):
	return render(request, 'shop/home.html')

def product(request):
	return render(request, 'shop/product.html')