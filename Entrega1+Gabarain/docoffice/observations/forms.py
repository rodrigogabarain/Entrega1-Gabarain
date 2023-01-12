from django import forms

class ObservationForm(forms.Form):
    dni = forms.CharField(max_length=11)
    observations = forms.CharField(max_length=1500)
    