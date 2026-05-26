
from django.db import models
from usuarios.models import Usuario



class Tarefa(models.Model):
    # Lista de valores válidos para o campo 'status'.
    # Cada tupla tem: (valor salvo no banco, texto exibido ao usuário).
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),

        ('CONCLUIDA' , 'Concluida'),
        ('CANCELADA' , 'Cancelada')
    ]
    
    PRIORIDADE_CHOICES ={
        ('URGENTE' , 'Urgente'),
        ('NAO_URGENTE' , 'Não urgente')
    }
    


    # Título da tarefa — texto curto, limitado a 255 caracteres.
    titulo = models.CharField(max_length=255)

    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    prioridade = models.CharField(max_length=40 , choices=PRIORIDADE_CHOICES, default='NAO_URGENTE')
    usuario_responsavel = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.titulo


