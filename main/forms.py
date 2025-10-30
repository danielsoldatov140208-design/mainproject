from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UnlUser


class UnlRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = UnlUser
        fields = ['username', 'email', 'password1', 'password2']
