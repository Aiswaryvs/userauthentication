from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager

# Create your models here.

"""User model"""
class UserManager(BaseUserManager):
    def create_user(self, email, username,first_name,last_name ,mobilephone, password=None):
        
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name ,
            mobilephone=mobilephone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,first_name,last_name ,mobilephone, password=None):
        
        user = self.create_user(
            email,
            password = password,
            username = username,
            first_name=first_name,
            last_name=last_name ,
            mobilephone=mobilephone
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    mobilephone = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name', 'mobilephone']


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    def __str__(self):
        return self.first_name




    