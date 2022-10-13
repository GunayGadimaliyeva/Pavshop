import email
from django import forms 
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','phone', 'password1', 'password2','address1', 'address2', 'country', 'town', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_class ={
                'placeholder': f'{self.fields[str(_(field))].label}'
            }
            self.fields[str(field)].widget.attrs.update(
                new_class
            )

    def save(self, commit=True):
        instance = super(RegisterForm, self).save(commit=False)
        import random
        n = random.randint(10,100)
        instance.username = f"{self.cleaned_data['first_name']}_{n}"
        if commit:
            instance.save()
        return instance

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    def clean(self) :
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username = username, password = password ):
            raise forms.ValidationError(_('Invalid login!'))

    
        



    