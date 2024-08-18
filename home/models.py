from django.db import models
from Users.models import Patient

# Create your models here.
class PatientData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=1)
    fat_percentual = models.DecimalField(max_digits=4, decimal_places=1)
    muscle_percentual = models.DecimalField(max_digits=4, decimal_places=1)
    hdl_colesterol = models.IntegerField()
    ldl_colesterol = models.IntegerField()
    total_colesterol = models.IntegerField()
    triglycerides = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.patient.name} - {self.date}"
