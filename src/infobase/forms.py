from django import forms

from .models import Entry

class EntryForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your title"
        })
    )
    summary = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "rows":2,
            "cols":60,
        })
    )
    c_amount = forms.IntegerField(initial=0, min_value=0)
    p_amount = forms.IntegerField(initial=0, min_value=0)
    quality = forms.IntegerField(initial=1, min_value=1, max_value=10)
    field_order = ['title', 'summary', 'c_amount', 'p_amount', 'quality']
    class Meta:
        model = Entry
        fields = {
            'title',
            'summary',
            'c_amount',
            'p_amount',
            'quality',
        }