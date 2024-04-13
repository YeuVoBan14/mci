from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoute),
    path('users/', views.getUsers),
    path('users/<str:pk>', views.getUser),
    path('users-create/', views.createUser),
    path('users-update/<str:pk>', views.updateUser),
    path('users-delete/<str:pk>', views.deleteUser),
    path('change-password/<str:pk>', views.changePassword),
    path('login/', views.loginPage),

    path('jobs/', views.getJobs),
    path('jobs/<str:pk>', views.getJob),
    path('jobs-create/', views.createJob),
    path('jobs-update/<str:pk>', views.updateJob),
    path('jobs-delete/<str:pk>', views.deleteJob),
    path('jobs-filter/', views.filterJobs),
    path('jobs-datefilter/', views.filterDateJobs),
    path('jobs-applicants/', views.getJobswithApplicants),
]