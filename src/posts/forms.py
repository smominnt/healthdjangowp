from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm): # form used for creating and editing a Post
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your title"
        })
    )
    file = forms.FileField(
        label='Select image',
        help_text='max. 42mb',
        required=False
    )
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "rows":4,
            "cols":120,
        })
    )
    field_order = ['title', 'file', 'content']
    class Meta:
        model = Post
        fields = {
            'title',
            'file',
            'content'
        }

class CommentForm(forms.ModelForm): # form used for submitting comments
    class Meta:
        model = Comment
        fields = {
            'content'
        }
