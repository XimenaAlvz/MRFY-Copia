from django import forms
from .models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())  # Campo para confirmar contraseña

    class Meta:
        model = User
        fields = ['Correo', 'IDUsuario', 'Password']  # Campos del formulario de registro
        widgets = {
            'Correo': forms.TextInput(attrs={'class': 'input__box'}),
            'Password': forms.PasswordInput(),  # Asegura que la contraseña se oculta
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('Password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden.")

        return cleaned_data
