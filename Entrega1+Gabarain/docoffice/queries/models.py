from django.db import models

# Create your models here.
class Queries(models.Model):
    dni=models.CharField(max_length=11)
    n_query  = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    age = models.FloatField()
    
    vaccines = models.BooleanField(default=True)

    def __str__(self):
        return self.dni

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural ='Consultas'