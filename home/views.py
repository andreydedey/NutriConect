from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Users.models import Patient
from .models import PatientData
from datetime import datetime


# Create your views here.
@login_required
def patients(request):
    patients = Patient.objects.filter(nutritionist=request.user)
    return render(request, 'patients.html', {
        "patients": patients
    })


def register_patient(request):

    sex = request.POST.get('sex').strip()
    name = request.POST.get('name').strip()
    age = request.POST.get('age').strip()
    email = request.POST.get('email').strip()
    tel = request.POST.get('tel').strip()

    patients = Patient.objects.filter(email=email)
    if patients.exists():
        messages.add_message(request, messages.constants.ERROR, f'A patient with the email {email} is already registred, please use another')
        return redirect(reverse('patients'))
    
    try:
        patient = Patient(
            name=name,
            age=age,
            email=email,
            tel=tel,
            sex=sex,
            nutritionist=request.user
        )

        patient.save()
    # Can add logic of duplicate patients here!
    except Exception as e:
        print(e)

    messages.add_message(request, messages.constants.SUCCESS, 'Patient registered with success')
    return redirect(reverse('patients'))


@login_required
def patient_data(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
    except Exception as e:
        print(e)

    if not patient.nutritionist == request.user:
        messages.add_message(request, messages.constants.ERROR, 'This is not your patient')
        return redirect(reverse('patients'))

    return render(request, 'patient_data.html', {
        "patient": patient
    })


def register_patient_data(request):
    weight = request.POST.get('weight')
    height = request.POST.get('height')
    fatPercentual = request.POST.get('fatPercentual')
    musclePercentual = request.POST.get('musclePercentual')
    hdlColesterol = request.POST.get('hdlColesterol')
    ldlColesterol = request.POST.get('ldlColesterol')
    totalColesterol = request.POST.get('totalColesterol')
    tryglycerides = request.POST.get('tryglycerides')

    try:
        patient_data = PatientData (
            # patient = patient.id
            date=datetime.now().date().strftime('%Y-%m-%d'),
            weight=weight,
            height=height,
            fat_Percentual=fatPercentual,
            muscle_percentual=musclePercentual,
            hdl_colesterol=hdlColesterol,
            ldl_colesterol=ldlColesterol,
            total_colesterol=totalColesterol,
            tryglycerides=tryglycerides
        )

        patient_data.save()
    except Exception as e:
        print(e)
    

@login_required
def list_patients(request):
    patients = Patient.objects.filter(nutritionist=request.user)
    return render(request, 'list_patients.html', {
        "patients": patients
    })
