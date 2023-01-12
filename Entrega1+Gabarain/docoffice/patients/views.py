from django.shortcuts import render
from django.http import HttpResponse

from patients.models import Patients
from patients.forms import PatientForm

# Create your views here.
def create_patient(request):
    if request.method =='GET':
        context = {
            'form' : PatientForm()
        }

        return render(request, 'patients/create_patient.html',context=context)

    elif request.method == 'POST' :
        form=PatientForm(request.POST)
        if form.is_valid():
            Patients.objects.create(
                name = form.cleaned_data['name'],
                address = form.cleaned_data['address'],
                dni = form.cleaned_data['dni'],
                
                first_query = form.cleaned_data['first_query'],
            )
            context ={
                'message': 'Pasiente cargado con exito'
            }
            return render(request, 'patients/create_patient.html' , context=context)
        else:
            context = {
                'form_errors' : form.errors,
                'form' :PatientForm()
            }
            return render (request,'patients/create_patient.html',context=context)

def list_patients(request):
    if 'search' in request.GET:
        search =request.GET['search']
        patients=Patients.objects.filter(name__icontains=search)
    else:
        patients=Patients.objects.all()
    context ={
        'patients': patients,
    }
    return render(request, 'patients/list_patients.html',context=context )

