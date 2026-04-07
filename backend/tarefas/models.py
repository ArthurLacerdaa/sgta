from django.db import models

# Define como os dados são armazenados, similar as tabelas do banco.

class Tarefa(models.Model):
    STATUS_CHOICE = {
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA' , 'Concluida'),
        ('CANCELADA' , 'Cancelada')
    }

    PRIORIDADE_CHOICES ={
        ('URGENTE' , 'Urgente'),
        ('NAO_URGENTE' , 'Não urgente')
    }


    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='ABERTA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    prioridade = models.CharField(max_length=40 , choices=PRIORIDADE_CHOICES, default='NAO_URGENTE')

    
    def __str__(self):
        return self.titulo
