# from dataclasses import fields
from django.core.exceptions import ValidationError
from django import forms 
from .models import ContactMessage

# widget=forms.Textarea(
#             attrs= {
#                 'class': 'form-control',
#                 'rows': 10
#             }
#     )

# class ContactForm(forms.Form):
#     full_name = forms.CharField()
#     email = forms.EmailField()
#     phone = forms.IntegerField()
#     subject = forms.CharField()
#     message = forms.CharField()

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'subject', 'message']
        # yaxud:
        # fields=  '__all__'
        # yaxud:
        # exclude = ["email"]           # emailden bashqa hamisi cixacaq sehifemizde
        # Ayri-ayri heresine widget yazmaq istesek:
        # widgets ={
        #     'full_name': forms.TextInput(
        #         attrs = {
        #             'class': 'form-control'
        #         }
        #     )
        # }


    # Deyek ki, her birine 'form-control col-6' - bu classlari add etmek isteyirik, ayri-ayri widget yazmaq evezine:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_class ={
                'class': 'form-control col-6',
                'placeholder': f'Recipe your {self.fields[str(field)].label}'
            }
            self.fields[str(field)].widget.attrs.update(
                new_class
            )

    # def clean_email(self):
    #     if not self.cleaned_data['full_name'].endswith('rt'):
    #         raise ValidationError('Adinizi duz yazin dana')
