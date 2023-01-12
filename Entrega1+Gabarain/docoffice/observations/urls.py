from django.urls import path

from observations.views import create_observation,list_observations

urlpatterns = [
    path('create-observation/', create_observation),
    path('list-observations/', list_observations),
]