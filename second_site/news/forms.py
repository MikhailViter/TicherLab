from .models import Artiсles
from django.forms import ModelForm, TextInput,DateTimeInput,Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Artiсles
        fields =  ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title' : TextInput (attrs={
                'class' : 'form control',
                'placeholder' : "Название статьи"
        }),
            'anons': TextInput (attrs={
                'class': 'form control',
                'placeholder': "Анонс"
            }),
            'full_text': Textarea (attrs={
                'class': 'form control',
                'placeholder': "Текст статьи"
            }),
            'date': DateTimeInput (attrs={
                'class': 'form control',
                'placeholder': "Дата публикации"
            }),

        }