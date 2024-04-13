from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.auth.forms import UserCreationForm
from .models import Job, User
from .models import *
from django import forms
class UserForm(UserCreationForm):
    birth = forms.DateField(widget=forms.DateInput(attrs= {'type':'date', 'class':'form-control form-inline','placeholder':'Select date of birth'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Enter Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Confirm Password"}))
    class Meta:
        model = User
        fields = ['username','password1','password2','name','birth', 'school', 'hometown','email', 'profile_picture']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'school':forms.TextInput(attrs={'class':'form-control', 'placeholder':'School'}),
            'hometown':forms.TextInput(attrs={'class':'form-control', 'placeholder':'hometown'}),
            'email':forms.TextInput(attrs={'type':'email','class':'form-control', 'placeholder':'Email address'}),
            'profile_picture':forms.FileInput()
        }
class UpdateUserForm(ModelForm):
    birth = forms.DateField(widget=forms.DateInput(attrs= {'type':'date', 'class':'form-control form-inline','placeholder':'Select date of birth'}))
    class Meta:
        model = User
        fields = ['username', 'name', 'birth', 'school', 'hometown','email', 'profile_picture']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'school':forms.TextInput(attrs={'class':'form-control', 'placeholder':'School'}),
            'hometown':forms.TextInput(attrs={'class':'form-control', 'placeholder':'hometown'}),
            'email':forms.TextInput(attrs={'type':'email','class':'form-control', 'placeholder':'Email address'}),
            'profile_picture':forms.FileInput()
        }
class JobForm(ModelForm):
    applicants = ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    class Meta:
        model = Job
        fields='__all__'
        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title'}),
            'description': forms.Textarea(attrs={'rows':5, 'class':'form-control', 'placeholder':'Enter title'}),
        }