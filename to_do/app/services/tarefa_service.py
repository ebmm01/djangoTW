from ..models import Tarefas

def cadastrar_tarefa(tarefa):
    
    Tarefas.objects.create(
        titulo = tarefa.titulo,
        descricao = tarefa.descricao,
        data_expiracao = tarefa.data_expiracao,
        prioridade = tarefa.prioridade
    )