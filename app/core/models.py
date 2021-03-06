from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email ID is required')
        user=self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class UserModel(AbstractBaseUser,PermissionsMixin):

    email=models.EmailField(max_length=250,unique=True)
    name=models.CharField(max_length=250)
    is_user=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='email'
