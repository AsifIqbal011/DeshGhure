from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,authenticate ,logout as auth_logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, template_name='TestApp/home.html')

def destination(request):
    return render(request, template_name='TestApp/destination.html')

def package(request):
    packages=Package.objects.all()
    context={'packages': packages}
    return render(request, template_name='TestApp/package.html',context=context)

def review(request):
    reviews=Review.objects.all()
    context={'reviews': reviews}
    return render(request, template_name='TestApp/review.html',context=context)

@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        location_id = request.POST.get("location")
        status = request.POST.get("status")  # 'visited' or 'wishlist'
        
        # Make sure to use the actual Location object
        location = Location.objects.get(id=location_id)

        BucketList.objects.update_or_create(
            user=request.user,
            location=location,
            defaults={'status': status}
        )
        return redirect('profile')  # only redirect after POST

    # GET method: show profile page
    locations = Location.objects.all()
    user_bucketlist = BucketList.objects.filter(user=request.user)
    user_profile = Profile.objects.get(user=request.user)

    visited_spots = BucketList.objects.filter(user=request.user, status='visited').count()
    wishlist_spots = BucketList.objects.filter(user=request.user, status='wishlist').count()
    
    context = {
        'locations': locations,
        'visited_spots': visited_spots,
        'wishlist_spots': wishlist_spots,
        'user_bucketlist': user_bucketlist,
        'profile': user_profile
    }
    return render(request, template_name='TestApp/profile.html', context=context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password")

    return render(request, template_name='TestApp/login.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        profile_pic = request.FILES.get('profile_pic')

        if password1 != password2:
            return render(request, 'TestApp/registration.html', {'error': "Passwords do not match"})

        user = User.objects.create_user(username=username, email=email, password=password1)
        Profile.objects.create(user=user, phone=phone, bio=bio, profile_pic=profile_pic)
        auth_login(request, user)
        return redirect('home') 
    return render(request, template_name='TestApp/registration.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')

@login_required
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

def division_detail(request, name):
    context={'division': name.capitalize()}
    return render(request, template_name='TestApp/division_detail.html',context=context)

def update_bucket_list(request):
    if request.method == 'POST':
        location_name = request.POST.get('location')
        status = request.POST.get('status')  # 'visited' or 'wishlist'

        location, created = Location.objects.get_or_create(name=location_name)
        BucketList.objects.update_or_create(
            user=request.user,
            location=location,
            defaults={'status': status}
        )
        return redirect('profile')