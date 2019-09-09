from django.shortcuts import render
from app.forms import TarefaForm

# Create your views here.

def listar_tarefas(request):
    return render(request, 'tarefas/listar_tarefas.html')

def cadastrar_tarefa(request):
    form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})