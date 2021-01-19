# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    typeUser = [
        ('admin', 'admin'),
        ('user', 'user'),
    ]
    type = models.CharField(max_length=15, choices=typeUser, default='user')

    def __str__(self):
        return self.username
