from django.shortcuts import render
from django.http import HttpResponse

from observations.models import Observations
from observations.forms import ObservationForm

# Create your views here.
def create_observation(request):
    if request.method =='GET':
        context = {
            'form' : ObservationForm()
        }

    elif request.method == 'POST' :
        form=ObservationForm(request.POST)
        if form.is_valid():
            Observations.objects.create(
                dni = form.cleaned_data['dni'],
                observations = form.cleaned_data['observations'], 
            )
            context ={
                'message': 'Cargada nueva observacion'
            }
        else:
            context = {
                'form_errors' : form.errors,
                'form' :ObservationForm()
            }
    return render (request,'observations/create_observation.html',context=context)

def list_observations(request):
    if 'search' in request.GET:
        search =request.GET['search']
        observations =Observations.objects.filter(dni__icontains=search)
    else:
        observations = Observations.objects.all()
    context ={
        'observations': observations,
    }
    return render(request, 'observations/list_observations.html',context=context )









































