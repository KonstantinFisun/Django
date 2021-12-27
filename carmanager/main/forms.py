from .models import Transport,Type_transport,Firm
from django.forms import ModelForm, TextInput, Textarea

class TransportForm(ModelForm):
    class Meta:
        model = Transport
        fields = ['id_firm', 'id_type', 'model', 'weight', 'power']

        widgets = {
            "id_firm": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID фирмы'
            }),
            "id_type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID типа'
            }),
            "model": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название модели'
            }),
            "weight": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес'
            }),
            "power": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Мощность(л.с.)'
            })
        }


class FirmForm(ModelForm):
    class Meta:
        model = Firm
        fields = ['title', 'country']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Название фирмы'
            }),
            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            })
        }

class TypeForm(ModelForm):
    class Meta:
        model = Type_transport
        fields = ['title']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Тип транспорта'
            })
        }

# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ["title", "task"]
#         widgets = {
#             "title": TextInput(attrs =
#             {
#                 'class' : 'form-control',
#                 'placeholder': 'Введите название'
#             }),
#             "task": Textarea(attrs=
#             {
#                 'class': 'form-control',
#                 'placeholder': 'Введите описание'
#             }),
#         }
