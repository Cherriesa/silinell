from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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
    
class incident(models.Model):
    STATUS_ACTION_CHOICES = (
        ('I', 'Identified'),
        ('W', 'watch'),
        ('F', 'fixed'),
        ('F', 'investigating'),
    )
    STATUS_UPTIME_CHOICES = (
        ('D', 'Down'),
        ('U', 'up'),
     
    )
    status_action = models.CharField(max_length=1, choices= STATUS_ACTION_CHOICES )
    status_webstie = models.CharField(max_length=1, choices= STATUS_UPTIME_CHOICES)
    website_name = models.CharField(max_length=50)
    url = models.CharField(max_length=30, blank=True)
    message  = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
     return self.website_name

