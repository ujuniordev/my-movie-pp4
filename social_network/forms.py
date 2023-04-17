from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class PostForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Post
        exclude = ("user", )