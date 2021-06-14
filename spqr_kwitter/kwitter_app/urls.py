from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('enter/', views.enter),
    path('login/', views.login),
    path('profile', views.profile),
    path('register/', views.register),
    path('dashboard', views.dashboard),
    path('success/', views.success),
    path('logout', views.logout),
    path('edit/', views.edit, name='edit'),
]