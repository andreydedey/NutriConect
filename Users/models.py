from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    is_nutritionist = models.BooleanField(default=False)


class Admin(Users):
    pass


class Nutritionist(Users):
    nutritionist_groups = models.ManyToManyField(
        'auth.Group',
        related_name='nutritionist_set',
        blank=True
    )
    nutritionist_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='nutritionist_permissions',
        blank=True
    )


class Patient(Users):
    patient_nutritionist = models.ForeignKey(
        Nutritionist, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    patient_groups = models.ManyToManyField(
        'auth.Group',
        related_name='patient_set',
        blank=True
    )
    patient_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='patient_permissions',
        blank=True
    )
