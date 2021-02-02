from django.shortcuts import render

def home(request):
	return render(request, 'shop/home.html')

def about(request):
	return render(request, 'shop/about.html')