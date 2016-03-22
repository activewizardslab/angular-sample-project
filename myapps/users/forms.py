from django import forms

from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    first_name = forms.CharField(min_length=1, max_length=64)
    last_name = forms.CharField(min_length=1, max_length=64)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=30)
    confirm_password = forms.CharField(min_length=8, max_length=30)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exists.')

        return email

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError('Paswords don\'t match.')

class EmailForm(forms.Form):
    email = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exists.')

        return email

class SettingsForm(forms.Form):
    first_name = forms.CharField(min_length=1, max_length=64)
    last_name = forms.CharField(min_length=1, max_length=64)

class ForgotPwdForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if not user.exists():
            raise forms.ValidationError('User with this email is not exists.')

        self.user = user.get()
        return email

class ConfirmationPwdForm(forms.Form):
    password = forms.CharField(min_length=8, max_length=30)
    confirm_password = forms.CharField(min_length=8, max_length=30)

    def clean(self):
        cleaned_data = super(ConfirmationPwdForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError('Paswords don\'t match.')
