from django.db import models
from django.contrib.auth.models import User


class Tarefas(models.Model):

    PRIORIDADES_CHOICES = [
        ("A", "Alta"),
        ("N", "Normal"),
        ("B", "Baixa"),
    ]

    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    data_expiracao = models.DateField(null=False, blank=False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADES_CHOICES, null=False, blank=False)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)