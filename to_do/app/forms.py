from django import forms
from .models import Tarefas

class TarefaForm(forms.ModelForm):
    
    class Meta:
        model = Tarefas
        exclude = ('usuario',)
        fields = '__all__'