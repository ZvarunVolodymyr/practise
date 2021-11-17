from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


# class UserManaget(BaseUserManager):
#     def create_user(self, email, password=None):
#         if email is None:
#             raise TypeError('пошта має існувати')
#
#
#
#
#
# class User(models.Model):
#     id_of_certificate = models.IntegerField(unique=True)
#     first_name = models.CharField(max_length=70)
#     last_name = models.CharField(max_length=70)
#     email = models.EmailField(max_length=70)
#     password = models.CharField(max_length=70)

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from user import security


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('пошта пуста')
        try:
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        except:
            raise

    def create_common_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id_of_certificate = models.IntegerField(unique=True)
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id_of_certificate', 'first_name', 'last_name', 'password']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self