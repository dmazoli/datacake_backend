from datetime import datetime
from django.db import models
from django.utils import timezone

class TodoModel(models.Model): 
    nome = models.CharField(verbose_name="Tarefa", max_length=250)
    inicio = models.DateField(verbose_name="Data de início", default=datetime.now)
    fim = models.DateField(verbose_name="Data final", default=datetime.now)
    status = models.BooleanField(verbose_name="Finalizado?")
    class Meta:
        ordering = ["-inicio"]
    def __str__(self):
        return self.nome
