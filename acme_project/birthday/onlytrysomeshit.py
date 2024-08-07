from django import forms

from .models import Contest


class ContestForm(forms.ModelForm):
    
    class Meta:
        model = Contest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea({'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea({'cols': '22', 'rows': '5'}),
        }



from django.db import models


class Contest(models.Model):
    title = forms.CharField(label='Название', max_length=20)
    description = forms.TextField('Описание')
    price = forms.IntegerField(
        'Цена',
        validators=[MinValueValidator(1), MaxValueValidator(9)],
        help_text='Рекомендованная розничная цена',
    )
    comment = forms.TextField(
        'Комментарий',
        blank=True,
    )