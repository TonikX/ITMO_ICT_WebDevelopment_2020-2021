from .models import Driver, Car
from django.forms import ModelForm, TextInput


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = [
            "optional_information",
            "first_name",
            "last_name",
            "date_of_birthday",
        ]
        widgets={
            "first_name": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "date_of_birthday": TextInput(attrs={
                'class': 'form-control',
            })
         }


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = [
        "id_number",
        "model",
        "label",
        "color"
        ]
        widgets={
            "id_number": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите ID'
            }),
            "model": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Модель'
            }),
            "label": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите label'
            }),
            "color": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите color'
            })
         }
