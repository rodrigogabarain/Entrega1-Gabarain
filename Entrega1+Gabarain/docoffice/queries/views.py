from django.shortcuts import render
from django.http import HttpResponse

from queries.models import Queries
from queries.forms import QueryForm

# Create your views here.
def create_query(request):
    if request.method =='GET':
        context = {
            'form' : QueryForm()
        }

        return render(request, 'queries/create_query.html',context=context)

    elif request.method == 'POST' :
        form=QueryForm(request.POST)
        if form.is_valid():
            Queries.objects.create(
                dni= form.cleaned_data['dni'],
                n_query= form.cleaned_data['n_query'],
                weight= form.cleaned_data['weight'],
                height= form.cleaned_data['height'],
                age= form.cleaned_data['age'],
                
                vaccines= form.cleaned_data['vaccines'],
            )
            context ={
                'message': 'Datos cargados'
            }
        else:
            context = {
                'form_errors' : form.errors,
                'form' :QueryForm()
            }
        return render (request,'queries/create_query.html', context=context)

def list_queries(request):
    if 'search' in request.GET:
        search = request.GET['search']
        queries = Queries.objects.filter(dni__icontains=search)
    else:
        queries = Queries.objects.all()
    context ={
        'queries':queries,
    }
    return render(request, 'queries/list_queries.html', context=context )
