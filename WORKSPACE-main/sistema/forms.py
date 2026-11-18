from django import forms
from sistema.models import *
 
# Checagem de email
# checagem de senha
# checagem de dado inserido

ESPECIALIDADES = [
    ('CARTIOLOGIA', 'Cardiologia'),
    ('DERMATOLOGIA', 'Dermatologia'),
    ('ENDOCRINOLOGIA', 'Endocrinologia'),
    ('GASTROENTEROLOGIA', 'Gastroenterologia'),
    ('NEUROLOGIA', 'Neurologia'),
    ('ORTOPEDIA', 'Ortopedia'),
    ('PEDIATRIA', 'Pediatria'),
]

class MedicoForm(forms.ModelForm):
    especialidade = forms.ChoiceField(
        choices = ['', 'Selecione uma especialidade'] + ESPECIALIDADES,
        label = 'Especialidade',
    )

    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'crm', 'especialidade']

        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'Email',
            'telefone': 'Telefone',
            'crm': 'CRM',
            'especialidade': 'Especialidade'
        }