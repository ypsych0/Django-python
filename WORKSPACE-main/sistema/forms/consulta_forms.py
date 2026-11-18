from django import forms
from sistema.models import Consulta

class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data_consulta', 'status', 'observacao']

        labels = {
            'paciente': 'Paciente',
            'medico': 'Médico',
            'data_consulta': 'Data e horário',
            'status': 'Status',
            'observacao': 'Observação'
        }