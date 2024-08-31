from django.urls import path
from . import views

urlpatterns = [
    path('patients', views.patients, name='patients'),
    path('register_patient', views.register_patient, name='register_patient'),
    path('list_patients', views.list_patients, name='list_patients'),
    path('patient_data/<str:patient_id>', views.patient_data, name='patient_data'),
    path('register_patient_data/<str:patient_id>', views.register_patient_data, name='register_patient_data'),
    path('weight_graphic/<str:id>', views.weight_graphic, name='weight_graphic'),
]