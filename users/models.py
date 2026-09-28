from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    avatar = models.ImageField(upload_to="photos", blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
