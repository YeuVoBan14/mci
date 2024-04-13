from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('users/', views.userPage, name='userPage'),
    path('users/add', views.addUser, name='addUser'),
    path('users/edit/<str:pk>', views.updateUser, name='updateUser'),
    path('users/delete/<str:pk>', views.deleteUser, name='deleteUser'),

    path('jobs/', views.jobPage, name='jobPage'),
    path('jobs/add', views.addJob, name='addJob'),
    path('jobs/edit/<str:pk>', views.updateJob, name='updateJob'),
    path('jobs/delete/<str:pk>', views.deleteJob, name='deleteJob'),
]