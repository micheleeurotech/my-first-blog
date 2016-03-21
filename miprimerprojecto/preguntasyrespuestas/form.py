from django import forms
from preguntasyrespuestas.models import Pregunta


class PreguntaForm(forms.ModelForm):
	class Meta:
		model = Pregunta
		fields = '__all__'

#class PreguntaForm(forms.Form):
	#asunto = forms.CharField(max_length=100, required = True)
	#descripcion = forms.CharField(widget=forms.Textarea, required = True)
