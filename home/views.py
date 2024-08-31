from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Users.models import Patient
from .models import PatientData
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt


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
def list_patients(request):
    patients = Patient.objects.filter(nutritionist=request.user)
    return render(request, 'list_patients.html', {
        "patients": patients
    })


@login_required
def patient_data(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
    except Exception as e:
        print(e)

    if not patient.nutritionist == request.user:
        messages.add_message(request, messages.constants.ERROR, 'This is not your patient')
        return redirect(reverse('patients'))
    
    try:
        patient_data = PatientData.objects.filter(patient=patient_id)
    except(ObjectDoesNotExist):
        patient_data = None

    return render(request, 'patient_data.html', {
        "patient": patient,
        "patient_data": patient_data
    })


def register_patient_data(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    weight = request.POST.get('weight')
    height = request.POST.get('height')
    fatPercentual = request.POST.get('fatPercentual')
    musclePercentual = request.POST.get('musclePercentual')
    hdlColesterol = request.POST.get('hdl')
    ldlColesterol = request.POST.get('ldl')
    totalColesterol = request.POST.get('ctotal')
    tryglycerides = request.POST.get('triglycerides')

    try:
        patient_data = PatientData (
            patient = patient,
            date=datetime.now().date().strftime('%Y-%m-%d'),
            weight=weight,
            height=height,
            fat_percentual=fatPercentual,
            muscle_percentual=musclePercentual,
            hdl_colesterol=hdlColesterol,
            ldl_colesterol=ldlColesterol,
            total_colesterol=totalColesterol,
            triglycerides=tryglycerides
        )

        patient_data.save()
        print('salvou')
    except Exception as e:
        print(e)

    return redirect(reverse('patient_data', args=[patient_id]))
    

@login_required
@csrf_exempt
def weight_graphic(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    data = PatientData.objects.filter(patient=patient).order_by("date")
    
    weights = [patient_data.weight for patient_data in data]
    labels = list(range(len(weights)))
    
    patient_weight_data = {
        'weights': weights,
        'labels': labels
    }
    return JsonResponse(patient_weight_data)
