from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image', 'audio']
        labels = {'text': 'Текст поста', 'image': 'Картинка', 'audio': 'Трек'}