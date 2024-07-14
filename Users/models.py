from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Patient(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino')
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100, unique=True)
    tel = models.CharField(max_length=15)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    nutritionist = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
