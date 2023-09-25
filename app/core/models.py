"""
Database models
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,password=None,**extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password) # encrypt password
        user.save(using=self._db) # save user to database

        return user

    def create_superuser(self,email,password):
        """Create and return a new superuser."""
        user = self.create_user(email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # is user active?
    is_staff = models.BooleanField(default=False) # is user staff?

    objects = UserManager() # user manager

    USERNAME_FIELD = 'email' # email is the username
