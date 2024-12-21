from django.contrib import admin
from .models import Medico, Paciente, Consulta

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Consulta)