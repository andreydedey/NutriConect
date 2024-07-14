from django.contrib import admin
from .models import CustomUser, Patient

# Register your models here.
@admin.register(CustomUser)
class NutritionistAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

