from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Location,Package,Review,Profile,BucketList])