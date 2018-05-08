"""databaseProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.contrib.auth import views as auth_views

from travellite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    #path('login/', auth_views.login, {'template_name': 'login.html'}),
    path('signup/', views.signup, name='signup'),
    path('trains/', views.trains, name='trains'),
    path('hotels/', views.hotels, name='hotels'),
    path('explore/', views.explore, name='explore'),
    path('book/', views.book, name='book'),
    path('account/', views.account, name='account'),
    path('reviews/', views.reviews, name='reviews'),
    path('logout/', views.logout, name='logout')
]
