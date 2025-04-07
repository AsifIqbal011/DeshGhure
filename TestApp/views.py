from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, template_name='TestApp/home.html')

def destination(request):
    return render(request, template_name='TestApp/destination.html')

def package(request):
    return render(request, template_name='TestApp/package.html')

def review(request):
    return render(request, template_name='TestApp/review.html')

def profile(request):
    return render(request, template_name='TestApp/profile.html')