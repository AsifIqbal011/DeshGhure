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