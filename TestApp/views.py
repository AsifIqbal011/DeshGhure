from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    return render(request, template_name='TestApp/home.html')

def destination(request):
    return render(request, template_name='TestApp/destination.html')

def package(request):
    return render(request, template_name='TestApp/package.html')

def review(request):
    reviews=Review.objects.all()
    context={'reviews': reviews}
    return render(request, template_name='TestApp/review.html',context=context)

def profile(request):
    return render(request, template_name='TestApp/profile.html')

def review_post(request):
    if request.method=="POST":
        data = request.POST

        location=data.get('location')
        rating =data.get('rating')
        details=data.get('details')
        reviewer_name=data.get('reviewer_name')
        review_date=data.get('review_date')
        review_img=request.FILES.get('review_img')

        Review.objects.create(
            location=location,
            rating =rating ,
            details=details,
            reviewer_name=reviewer_name,
            review_date=review_date,
            review_img=review_img,
        )
        return redirect('/review')

    reviews=Review.objects.all()
    context={'reviews': reviews}
    return render(request, template_name='TestApp/review_post.html',context=context)
