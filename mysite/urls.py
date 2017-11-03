"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required

from core import views as core_views
from personal import views as personal_views


urlpatterns = [
        url('^', include('django.contrib.auth.urls')),
        url(r'^admin/', admin.site.urls),
        url(r'^cartoons/',include('cartoons.urls',namespace='cartoons',app_name='cartoons')),
        url(r'^shows/',include('shows.urls',namespace='shows',app_name='shows')),
        url(r'^news_and_politics/',include('news_and_politics.urls',namespace='news_and_politics',app_name='news_and_politics')),
        url(r'^stand_up/',include('stand_up.urls',namespace='stand_up',app_name='stand_up')),
        url(r'^sports/',include('sports.urls',namespace='sports',app_name='sports')),
        url(r'^trending_movies/',include('trending_movies.urls',namespace='trending_movies',app_name='trending_movies')),
        url(r'^punjabi_movies/',include('punjabi_movies.urls',namespace='punjabi_movies',app_name='punjabi_movies')),
        url(r'^tracking/', include('tracking.urls')),
        ###for index page below format is used. In this case we have called it personal.urls
        url(r'^',include('personal.urls')),
       
     
        
        # Registration URLs
        url(r'^accounts/register/$',core_views.register, name='register'),
        url(r'^accounts/login/$', login, name='login'),
        url(r'^accounts/logout/$', logout, name='logout'),
        #url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),#
        url(r'^accounts/profile/$',login_required(personal_views.list_of_posts), name='allcategories'),
        
        #url(r'^accounts/register/complete/$',views.registration_complete, name='registration_complete'),""#
        url(r'^registration_complete/$', core_views.registration_complete, name='registration_complete'),
        url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
        ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
