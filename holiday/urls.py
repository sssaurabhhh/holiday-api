"""holiday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from django.conf.urls import url,include
from django.conf import settings
from rest_framework import routers
from loginauth import views
from client.api.viewsets import LeadsViewSet,CommentViewSet
from packages.api.viewsets import CountryViewSet


"""
Register REST API Routes via routers
"""
router = routers.DefaultRouter()

router.register(r'leads',LeadsViewSet,base_name='leads')
router.register(r'country',CountryViewSet,base_name='country')
router.register(r'comments',CommentViewSet,base_name='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
    url(r'^loginauth/',include('loginauth.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^accounts/login/$', views.user_login,name='login'),
    url(r'^api/', include(router.urls)),
]

