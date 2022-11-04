from django import forms 
from .models import Shipping_info, Billing_detail


class billingForm(forms.ModelForm):
    class Meta:
        model = Billing_detail
        fields = '__all__'
        widgets ={
            'Ship_to_a_different_address': forms.CheckboxInput()
        }


        
class shippingForm(forms.ModelForm):
    class Meta:
        
        model = Shipping_info
        exclude = ["billing_info"] 
        
        


