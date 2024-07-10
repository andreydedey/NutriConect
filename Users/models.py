from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    pass


class Patient(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino')
    ]

    username = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100, unique=True)
    tel = models.CharField(max_length=15)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    def __str__(self):
        return self.username
