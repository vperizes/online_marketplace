from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# user creation form has 3 feilds: username (comes from user model), password1 and password2
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your username",
                "class": "w-full py-2 px-6 rounded-xl",
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "marketplace@marketplace.com",
                "class": "w-full py-2 px-6 rounded-xl",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "w-full py-2 px-6 rounded-xl",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repeat Password",
                "class": "w-full py-2 px-6 rounded-xl",
            }
        )
    )
