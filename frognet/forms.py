from django import forms
from .models import Post, Coment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["name","description", "image"]


class ComentForm(forms.ModelForm):

    class Meta:
        model = Coment 
        fields = ["text"]