from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoute),
    path('users/', views.getUsers),
    path('users/<str:pk>', views.getUser),
    path('jobs/', views.getJobs),
    path('jobs/<str:pk>', views.getJob),
    path('jobs-create/', views.createJob, name='createJob'),
    path('jobs-update/<str:pk>', views.updateJob, name='updateJob'),
    path('jobs-delete/<str:pk>', views.deleteJob, name='deleteJob'),
]