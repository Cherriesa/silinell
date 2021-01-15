from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50 )
    email = models.EmailField(max_length=100, unique=True)

    username = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    session_token = models.CharField(max_length=10, default=0)

    active = models.BooleanField(default=True)
    # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # a superuser

    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    
class schedule_maintance(models.Model):
    name = models.CharField(max_length=40 )
    message = models.TextField(max_length=300, blank=True)
    when = models.DateTimeField(default=datetime.now, blank=True)
    
class component_group(models.Model):
    COLLAPSE_CHOICES = (
        ('Always expanded', 'Always expanded'),
        ('Always collapse', 'Always collapse'),
        ('Collapse but expand if there are issues', 'Collapse but expand if there are issues'),
    )
    name = models.CharField(max_length=40,blank=True)
    visibility = models.CharField(max_length=40,choices=COLLAPSE_CHOICES,default='Always expanded')
    Description =  models.TextField(max_length=300, blank=True)
    
    def __str__(self):
     return self.name

class component(models.Model):
    STATUS_CHOICES = (
        ('Operational', 'Operational'),
        ('Perfomance Issue', 'Perfomance Issue'),
        ('Partial Outage', 'Partial Outage'),
        ('Major Outage', 'Major Outage'),
    )
    name = models.CharField(max_length=40)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    Description =  models.TextField(max_length=300, blank=True)
    group = models.CharField(max_length=40, blank=True,null=True)
    when = models.DateTimeField(default=datetime.now, blank=True)
    link = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    enabled = models.BooleanField(default=True)
    
class incident(models.Model):
    STATUS_ACTION_CHOICES = (
        ('Identified', 'identified'),
        ('Watch', 'watch'),
        ('Fixed', 'fixed'),
        ('Investigating', 'investigating'),
    )
    STATUS_DOWNTIME_CHOICES = (
        ('Down', 'Down'),
        ('Up', 'up'),
     
    )
    STATUS_STICKED_CHOICES = (
        ('Stikced', 'Stikced'),
        ('Un Stikced', 'Un Stikced'),
     
    )
    STATUS_Visibility_CHOICES = (
        ('Viewable by public', 'Viewable by public'),
        ('Only logged in users can see', 'Only logged in users can see'),
     
    )
    status_action = models.CharField(max_length=40, choices= STATUS_ACTION_CHOICES )
    status_Downtime = models.CharField(max_length=40, choices= STATUS_DOWNTIME_CHOICES,default="Up" )
    Visibility = models.CharField(max_length=40, choices= STATUS_Visibility_CHOICES, default="Viewable by public" )
    stickied = models.CharField(max_length=40, choices= STATUS_STICKED_CHOICES, default="Stikced" )
    name = models.CharField(max_length=50)
    message  = models.TextField(max_length=300, blank=True)
    date_occur = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
     return self.name
 
  


    

