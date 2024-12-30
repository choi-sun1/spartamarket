from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms   
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import User


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get("password"):
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']