from django.urls import path

from queries.views import create_query ,list_queries

urlpatterns = [
    path('create-query/', create_query),
    path('list-queries/', list_queries),
]