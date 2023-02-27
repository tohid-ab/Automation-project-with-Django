from django import forms
from django.contrib.auth.models import User
from django.forms import Textarea, FileInput, TextInput
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("پسورد اشتباه است"))
        except User.DoesNotExist:
            self.add_error("username", forms.ValidationError("کاربر وجود ندارد"))
        return super().clean()
