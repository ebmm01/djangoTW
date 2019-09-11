from ..models import Tarefas

def cadastrar_tarefa(tarefa):
    
    Tarefas.objects.create(
        titulo = tarefa.titulo,
        descricao = tarefa.descricao,
        data_expiracao = tarefa.data_expiracao,
        prioridade = tarefa.prioridade,
        usuario = tarefa.usuario
    )

def listar_tarefas(usuario):
    return Tarefas.objects.filter(usuario=usuario).all()

def listar_tarefa_id(id):
    return Tarefas.objects.get(id=id)

def editar_tarefa(tarefa_bd, tarefa_nova):
    tarefa_bd.titulo = tarefa_nova.titulo
    tarefa_bd.descricao = tarefa_nova.descricao
    tarefa_bd.data_expiracao = tarefa_nova.data_expiracao
    tarefa_bd.prioridade = tarefa_nova.prioridade

    tarefa_bd.save(force_update=True)

def remover_tarefa(tarefa_bd):
    tarefa_bd.delete()