from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('follow/<str:username>/', views.follow_toggle, name='follow'),
    path('create/', views.create_post, name='create_post'),
]
