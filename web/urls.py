from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostDetailView

urlpatterns = [
     path('', views.home, name='web-home'),
     path('post/', views.post, name='web-post'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail')
]