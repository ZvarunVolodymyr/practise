from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from helping_func.validation_functions import validation

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password=None, **extra_fields):
        errors = []
        for i in extra_fields.keys():
            try:
                if i in ['is_superuser', 'is_staff']:
                    continue
                extra_fields[i] = validation(i, extra_fields)
            except ValueError as error:
                errors.append(error)
        try:
            password = validation('password', {'password':password})
        except ValueError as error:
            errors.append(error)
        if len(errors) != 0:
            print(errors)
            exit(0)
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('admin has to have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('admin has to have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # id_of_certificate = models.IntegerField(unique=True)
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'birth_date']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


class TokenBlackList(models.Model):
    token = models.CharField(max_length=400)
    exp = models.IntegerField()
