from django import forms

class PatientForm(forms.Form):
    name = forms.CharField(max_length=150)
    address = forms.CharField(max_length=50)
    dni =forms.CharField(max_length=11)

    first_query = forms.BooleanField(required=False)