from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=False, blank=False)
    birth = models.DateField(blank=True,null=True)
    school = models.CharField(blank=True,null=True, max_length=150)
    hometown = models.CharField(blank=True,null=True, max_length=150)
    email = models.EmailField(null=False, blank=False, unique=True)
    profile_picture = models.ImageField(null=True, blank=True, default='avatar.svg')
    def __str__(self):
        return self.username
class Job(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    applicants = models.ManyToManyField(User, blank=True)
    def short_description(self):
        return self.description[:50] if self.description else ''
    def __str__(self):
        return self.title