"""
URL configuration for Test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TestApp import views as t_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',t_views.home,name='home'),
    path('destination/', t_views.destination, name='destination'),  # destination Page
    path('package/', t_views.package, name='package'),  # package Page
    path('review/', t_views.review, name='review'),  # Review Page
    path('profile/', t_views.profile, name='profile'),  # Profile Page
    path('review_post/', t_views.review_post, name='review_post'),  # Profile Page
    path('login/', t_views.login_view, name='login'),  # login Page
    path('registration/', t_views.registration, name='registration'),  # registration Page
    path('division/<str:name>/', t_views.division_detail, name='division_detail'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
urlpatterns += staticfiles_urlpatterns()        