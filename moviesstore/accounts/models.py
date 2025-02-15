from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

# Create your models here.

class CustomUser(AbstractUser):
    security_question = models.CharField(max_length=255)
    security_answer = models.CharField(max_length=255)
    custom_groups = models.ManyToManyField(
        Group,
        related_name="custom_users",
        blank=True,
    )