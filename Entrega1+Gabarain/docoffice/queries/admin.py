from django.contrib import admin

# Register your models here.
from queries.models import Queries

# admin.site.register(Queries)

@admin.register(Queries)
class QueriesAdmin(admin.ModelAdmin):
    list_display = ('dni', 'n_query', 'weight', 'height', 'age','vaccines')
    
    search_fields = ('dni',)

















