from django import forms 
from .models import shipping_info, billing_detail


class billingForm(forms.ModelForm):
    class Meta:
        model = billing_detail
        fields = '__all__'
        widgets ={
            'Ship_to_a_different_address': forms.CheckboxInput()
        }


        
class shippingForm(forms.ModelForm):
    class Meta:
        
        model = shipping_info
        exclude = ["billing_info"] 
        
        


