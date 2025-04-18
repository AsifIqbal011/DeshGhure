from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Location(models.Model):
    location =models.CharField(max_length=100)

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
    location=models.CharField(max_length=100)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=5.0)
    details=models.TextField()
    reviewer_name=models.CharField(max_length=100,default="Traveler")
    review_date=models.DateTimeField(auto_now_add=True)
    review_img=models.ImageField(upload_to="review_pic")
    def __str__(self):
        return self.reviewer_name
    
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