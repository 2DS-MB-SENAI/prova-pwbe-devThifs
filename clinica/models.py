from django.db import models

status_choices = {
    (1, 'agendado'),
    (2, 'realizado'),
    (3, 'cancelado'),
}

especialidade_choices = {
    (1, 'medico'),
    (2, 'psicologo'),
    (3, 'oftamologista'),
}

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.IntegerField(choices=especialidade_choices)
    crm = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50, blank=True, null=True)

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_choices)

