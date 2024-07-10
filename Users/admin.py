from django.contrib import admin
from .models import Users, Patient

# Register your models here.
@admin.register(Users)
class NutritionistAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

