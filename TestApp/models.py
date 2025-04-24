from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Location_type(models.Model):
    type_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.type_name

class Location(models.Model):
    STATUS_CHOICES = [
        ('feature', 'Feature'),
        ('historical', 'Historical'),
        ('none', 'None'),
    ]

    location = models.CharField(max_length=100, unique=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    location_type = models.ForeignKey(Location_type, on_delete=models.SET_NULL, null=True)

    image = models.ImageField(upload_to='location_images/', blank=True, null=True)
    caption = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    best_time_to_visit = models.CharField(max_length=100, blank=True, null=True)
    cost_by_bus = models.IntegerField(default=0, help_text="Estimated cost by bus (৳)")
    cost_by_train = models.IntegerField(default=0, help_text="Estimated cost by train (৳)")
    cost_by_plane = models.IntegerField(default=0, help_text="Estimated cost by plane (৳)")

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='none',
        help_text="Label this location as Featured, Historical, or None"
    )

    def __str__(self):
        return self.location



class Package(models.Model):
    location =models.ForeignKey(Location,on_delete=models.CASCADE)
    caption =models.TextField()
    numofDay=models.IntegerField()
    numofPeople= models.IntegerField()
    rating = models.FloatField(default=5.0,validators=[MinValueValidator(1), MaxValueValidator(5)])
    price = models.IntegerField()
    package_img=models.ImageField(upload_to="package_pic", default="package_pic/default.jpg")

    def __str__(self):
        return self.caption

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=100)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=5.0)
    details = models.TextField()
    reviewer_name=models.CharField(max_length=100,null=True, blank=True)
    review_date=models.DateTimeField(auto_now_add=True)
    review_img = models.ImageField(upload_to='review_pic')

    def __str__(self):
        return f"{self.user.username} - {self.location}"    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username    
    
class BucketList(models.Model):
    VISIT_STATUS = [
        ('wishlist', 'Want to Visit'),
        ('visited', 'Visited'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=VISIT_STATUS)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'location']  # Prevent duplicate entries

    def __str__(self):
        return f"{self.user.username} - {self.location.location} - {self.get_status_display()}"