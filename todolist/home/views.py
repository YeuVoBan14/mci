from django.shortcuts import render, redirect
from .models import User, Job
from .forms import UserForm, UpdateUserForm, JobForm
from datetime import datetime
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home/home.html')
def userPage(request):
    pageView = 'users'
    users = User.objects.all()
    context = {'users':users, 'pageView':pageView}
    return render(request, 'home/home.html', context)
def addUser(request):
    pageView = 'add'
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            if form.birth > datetime.now().date():
                messages.error(request, 'Birth cant be in the future!')
                return redirect('addUser')
            else:
                form.save()
                messages.success(request, "Successfully added new user")
                return redirect('userPage')
        else:
            print(form.errors)
            messages.error(request, 'Please correct the error below.')
    context = {"form":form,'pageView':pageView}
    return render(request, 'home/user.html' ,context)
def updateUser(request,pk):
    pageView = 'edit'
    user = User.objects.get(id=pk)
    form = UpdateUserForm(instance=user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            if form.cleaned_data['birth'] > datetime.now().date():
                messages.error(request, 'Birth cant be in the future!')
                return redirect('updateUser', pk=user.id)
            else:
                form.save()
                instance = form.instance
                form = UpdateUserForm(instance=instance)
                messages.success(request,"Your customer has been updated")
            return redirect("userPage")
        else:
            messages.error(request,"Please correct the error below.")
            return redirect('updateUser', pk=user.id)
    context = {'form':form, 'pageView':pageView}
    return render(request, 'home/user.html', context)

def deleteUser(request, pk):
    pageView = 'delete'
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        messages.warning(request,'The selected user has been deleted!')
        return redirect('userPage')
    return render(request,'home/user.html',{'obj': user, 'pageView':pageView})

def jobPage(request):
    pageView = 'jobs'
    jobs = Job.objects.all()
    context = {'jobs':jobs, 'pageView':pageView}
    return render(request, 'home/home.html', context)
def addJob(request):
    pageView = 'add'
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added a new job!")
            return redirect('jobPage')
        else:
            messages.error(request,"Please correct the error below.")
            return redirect('addJob')
    context = { "form": form, 'pageView': pageView }
    return render(request, 'home/job.html', context)
def updateJob(request, pk):
    pageView = 'edit'
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            instance = form.instance
            form = JobForm(instance=instance)
            messages.success(request,"Your job has been updated")
            return redirect("jobPage")
        else:
            messages.error(request,"Please correct the error below.")
            return redirect('updateJob', pk=job.id)
    context = {'form':form, 'pageView':pageView}
    return render(request, 'home/job.html', context)
def deleteJob(request, pk):
    pageView = 'delete'
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        job.delete()
        messages.warning(request,'The selected job has been deleted!')
        return redirect('jobPage')
    return render(request,'home/job.html',{'obj': job, 'pageView':pageView})