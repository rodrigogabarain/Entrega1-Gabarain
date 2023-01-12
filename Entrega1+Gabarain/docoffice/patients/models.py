from django.db import models

# Create your models here.
class Patients(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=50)
    dni = models.CharField(max_length=11)
    first_query = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural ='Pacientes'
