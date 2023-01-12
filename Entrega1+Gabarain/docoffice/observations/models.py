from django.db import models

# Create your models here.
class Observations(models.Model):
    dni = models.CharField(max_length=11)
    observations = models.CharField(max_length=1500)


    
    
    def __str__(self):
        return self.dni

    class Meta:
        verbose_name = 'Observacion'
        verbose_name_plural ='Observaciones'
