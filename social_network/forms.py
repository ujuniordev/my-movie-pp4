from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("user", 'author')
