from django import forms
from sistema.models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf', 'mensagem']

        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'Email',
            'telefone': 'Telefone',
            'cpf': 'CPF',
            'mensagem': 'Mensagem'
        }