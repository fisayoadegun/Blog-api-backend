from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from .views import  UserCreateAPIView, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views



app_name = 'accounts'

urlpatterns = [
    #url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    #url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
