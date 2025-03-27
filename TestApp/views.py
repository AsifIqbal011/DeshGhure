from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, template_name='TestApp/home.html')

def about(request):
    return render(request, template_name='TestApp/about.html')

def contact(request):
    return render(request, template_name='TestApp/contact.html')

def review(request):
    return render(request, template_name='TestApp/review.html')