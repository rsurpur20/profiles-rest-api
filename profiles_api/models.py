from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, email, name, password = None):
        """create new user profile"""
        if not email: #if empty string or null
            raise ValueError("users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name = name) #creates new model object
        user.set_password(password) #makes sure password is secured, hashes it
        user.save(using=self._db) #saves to the current database

        return user

    def create_superuser(self, email, name, password):
        """create new super user user profile"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD  = 'email' #replace username field with email, this is a required field
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """get full name of user"""
        return self.name

    def get_short_name(self):
        """get short name of user"""
        return self.name

    def __str__(self):
        """ converts class to string, return string representation of user"""
        return self.email
    

