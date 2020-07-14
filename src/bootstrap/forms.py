from django import forms

from .models import Tdee

class BmrEntry(forms.ModelForm):
    weight = forms.IntegerField(required=True, initial=0, min_value=0, max_value=300)
    feet = forms.IntegerField(required=True, initial=0, min_value=0, max_value= 7)
    inches = forms.IntegerField(required=True, initial=0, min_value=0, max_value= 11)
    age = forms.IntegerField(required=True, initial=0, min_value=3, max_value=126)
    CHOICES = [(True,'Male'),
               (False,'Female')]
    sex = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    field_order = ['weight', 'feet', 'inches', 'age', 'sex']

    class Meta:
        model = Tdee
        fields = {
            'weight',
            'feet',
            'inches',
            'age',
            'sex'
        }
