from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Division,Location_type,Location,Package,Review,Profile,BucketList])