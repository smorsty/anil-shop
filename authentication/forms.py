from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    # вообще нужен email никнейм нахуй
    username = forms.CharField(label='E-mail', required=True)# name on site,
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f'User {username} does not exist!')

        if not self.user.check_password(password):
            raise forms.ValidationError(f'Password for {username} is not correct')

        return cleaned_data


#class RegisterForm(forms.Form):
 #   email = forms.EmailField(required=True)
