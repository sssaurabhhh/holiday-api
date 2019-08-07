from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'client'
urlpatterns = [
    url(r'^leads/$', views.LeadsView.as_view(), name='leads'),
]