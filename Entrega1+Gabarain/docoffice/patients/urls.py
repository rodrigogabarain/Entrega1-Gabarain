from django.urls import path

from patients.views import create_patient,list_patients

urlpatterns = [
    path('create-patient/', create_patient),
    path('list-patients/', list_patients),
]

