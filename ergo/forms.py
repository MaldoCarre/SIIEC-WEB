from django import forms
from.models import Ergometria
class FormularioErgometria(forms.ModelForm):
    
    class Meta:
        model = Ergometria
        fields = (
            'paciente_ergo',
            'ciclo_ergo',
            'banda_ergo',
            'carga',
            'fc_basal', 
            'tas_basal', 
            'tad_basal', 
            'fc_esfuerzo',
            'tas_esfuerzo', 
            'tad_esfuerzo', 
            'mets', 
            'st', 
            'st_mm', 
            'ta_plana', 
            'motivo_suspencion',
            'arritmia_sv',
            'arritmia_v',
            'sintomas',
            'fcm_edad',
            'percent_fcmp', 
            'itt',)


        labels={
            'paciente_ergo':'Paciente',
            'ciclo_ergo':'Cieclo ergo',
            'banda_ergo':'Banda Ergo',
            'carga':'Carga',
            'fc_basal':'Fc basal', 
            'tas_basal':'Tas basal', 
            'tad_basal':'Tad basal', 
            'fc_esfuerzo':'Fc esfuerzo',
            'tas_esfuerzo':'Tas esfuerzo', 
            'tad_esfuerzo':'Tad esfuerzo', 
            'mets':'Mets', 
            'st':'St', 
            'st_mm':'St mm', 
            'ta_plana':'Ta plana', 
            'motivo_suspencion':'Motivo de suspencion',
            'arritmia_sv':'Arritmia sv',
            'arritmia_v':'Arritmia v',
            'sintomas':'Sintomas',
            'fcm_edad':'Edad',
            'percent_fcmp':'Percent fcmp', 
            'itt':'ITT',
        }

        widgets={
            'paciente_ergo':forms.Select(attrs={'class':'form-control'}),
            'ciclo_ergo':forms.CheckboxInput(attrs={'class':'form-control' ,'style':'height:30px' }),
            'banda_ergo':forms.CheckboxInput(attrs={'class':'form-control' ,'style':'height:30px' }),
            'carga':forms.TextInput(attrs={'class':'form-control'}),
            'fc_basal':forms.TextInput(attrs={'class':'form-control'}), 
            'tas_basal':forms.TextInput(attrs={'class':'form-control'}), 
            'tad_basal':forms.TextInput(attrs={'class':'form-control'}), 
            'fc_esfuerzo':forms.TextInput(attrs={'class':'form-control'}),
            'tas_esfuerzo':forms.TextInput(attrs={'class':'form-control'}), 
            'tad_esfuerzo':forms.TextInput(attrs={'class':'form-control'}), 
            'mets':forms.TextInput(attrs={'class':'form-control'}), 
            'st':forms.TextInput(attrs={'class':'form-control'}), 
            'st_mm':forms.TextInput(attrs={'class':'form-control'}), 
            'ta_plana':forms.CheckboxInput(attrs={'class':'form-control' ,'style':'height:30px' }), 
            'motivo_suspencion':forms.TextInput(attrs={'class':'form-control'}),
            'arritmia_sv':forms.TextInput(attrs={'class':'form-control'}),
            'arritmia_v':forms.TextInput(attrs={'class':'form-control'}),
            'sintomas':forms.TextInput(attrs={'class':'form-control'}),
            'fcm_edad':forms.TextInput(attrs={'class':'form-control'}),
            'percent_fcmp':forms.TextInput(attrs={'class':'form-control'}), 
            'itt':forms.TextInput(attrs={'class':'form-control'}),
        }