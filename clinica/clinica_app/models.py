from django.db import models

# Create your models here.
class Medico(models.Model):
    nome_medico = models.CharField(max_length=50)
    celular = models.IntegerField()
    especialidade = models.CharField(max_length=50)
    crm = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome_medico

class Paciente(models.Model):
    nome_paciente = models.CharField(max_length=50)
    data_nascimento = models.DateField(null=True, blank=True)
    documento = models.CharField(max_length= 14, unique=True, null=True, blank=True)
    genero = models.CharField(max_length=10)
    celular = models.IntegerField(null=True)
    endereco = models.TextField(max_length=100)

    def __str__(self):
        return self.nome_paciente

class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.medico.nome_medico + "__"+self.paciente.nome_paciente