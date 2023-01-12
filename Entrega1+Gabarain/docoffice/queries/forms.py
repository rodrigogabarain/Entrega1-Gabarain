from django import forms

class QueryForm(forms.Form):
    dni = forms.CharField(max_length=11)
    n_query = forms.IntegerField()
    weight = forms.FloatField()
    height = forms.FloatField()
    age= forms.FloatField()

    vaccines = forms.BooleanField(required=False)