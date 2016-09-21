from django import forms


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.PasswordInput()
