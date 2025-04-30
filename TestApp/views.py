from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,authenticate ,logout as auth_logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

def home(request):
    featured_locations = Location.objects.filter(status='feature')
    historical_locations = Location.objects.filter(status='historical')
    context = {'featured_locations': featured_locations,
               'historical_locations': historical_locations,}
    return render(request, template_name='TestApp/home.html', context=context)

def destination(request):
    divisions = Division.objects.all()
    types = Location_type.objects.all()

    selected_division_id = request.GET.get('division')
    selected_type = request.GET.get('type')

    featured_locations = Location.objects.filter(status='feature')

    locations = Location.objects.all()

    if selected_type:
        locations = locations.filter(location_type__type_name=selected_type)
    
    if selected_division_id:
        locations = Location.objects.filter(division_id=selected_division_id)
    
        
    context ={'divisions': divisions,
              'types': types,
              'locations': locations,
              'featured_locations': featured_locations,
              'selected_division_id': int(selected_division_id) if selected_division_id else None,
              'selected_type': selected_type,}
    return render(request, 'TestApp/destination.html', context=context) 

def location_detail(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    context = {'location': location}
    return render(request, 'TestApp/location_detail.html',context=context)

def package(request):
    packages=Package.objects.all()
    context={'packages': packages}
    return render(request, template_name='TestApp/package.html',context=context)

@login_required
def package_detail(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    context={'package': package}
    return render(request, 'TestApp/package_detail.html', context=context)

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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        profile_pic = request.FILES.get('profile_pic')

        if password1 != password2:
            return render(request, 'TestApp/registration.html', {'error': "Passwords do not match"})

        user = User.objects.create_user(username=username, email=email, password=password1,first_name=first_name,last_name=last_name)
        Profile.objects.create(user=user, phone=phone, bio=bio, profile_pic=profile_pic)
        auth_login(request, user)
        return redirect('home') 
    return render(request, template_name='TestApp/registration.html')

@login_required
def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        profile.phone = request.POST.get('phone')
        profile.bio = request.POST.get('bio')
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
        profile.save()

        return redirect('profile')  # or any success page
    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'TestApp/edit_profile.html',context=context)

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
        reviewer_name = request.user.username
        review_date=data.get('review_date')
        review_img=request.FILES.get('review_img')

        Review.objects.create(
            user=request.user,
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

@login_required
def my_reviews(request):
    user_reviews = Review.objects.filter(user=request.user)
    context={'user_reviews': user_reviews}
    return render(request, 'TestApp/my_reviews.html', context=context)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == "POST":
        review.location = request.POST.get("location")
        review.rating = request.POST.get("rating")
        review.details = request.POST.get("details")
        review.review_date = datetime.date.today()

        if 'review_img' in request.FILES:
            review.review_img = request.FILES['review_img']

        review.save()
        return redirect('my_reviews')
    context={'review': review}
    return render(request, 'TestApp/edit_review.html', context=context)

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return redirect('my_reviews')

def division_detail(request, name):
    division = get_object_or_404(Division, name=name)
    locations = Location.objects.filter(division=division)
    context={ 'division': division,
             'locations': locations}
    return render(request, template_name='TestApp/division_detail.html',context=context)

@login_required
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
    
def book_package(request):
    messages.success(request, "✅ Booking Confirmed!")
    return redirect('package')    

def search_results(request):
    search_query = request.GET.get('search')
    results = []

    if search_query:
        results = Location.objects.filter(location__icontains=search_query)

    if search_query:
        results = Location.objects.filter(location__icontains=search_query)
        print(f"Search Query: {search_query}")
        print(f"Found {results.count()} results.")

    context = {
        'search_query': search_query,
        'results': results
    }
    return render(request, 'TestApp/search_results.html', context=context)