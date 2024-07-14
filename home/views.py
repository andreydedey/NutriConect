from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Users.models import Patient


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
def patient_data(request):
    return render(request, 'patient_data.html')
