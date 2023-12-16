from django import forms
from app.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields='__all__'
        #con la linea de abajo se puede personalizar 
        #los campos que desea
        #fields=['nombre','apellidos','email','estado']