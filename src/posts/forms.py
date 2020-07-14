from django import forms

from .models import Post

class PostForm(forms.ModelForm): # form used for creating and editing a Post
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your title"
        })
    )
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "rows":4,
            "cols":120,
        })
    )
    field_order = ['title', 'content']
    class Meta:
        model = Post
        fields = {
            'title',
            'content'
        }