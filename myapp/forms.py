from django import forms
from myapp import models


class contactform(forms.ModelForm):
    class Meta:
        model = models.contact
        fields = '__all__'
        
class buyerform(forms.ModelForm):
    class Meta:
        model = models.buyer
        fields = '__all__'
        
        
class sellerform(forms.ModelForm):
    class Meta:
        model = models.seller
        fields = '__all__'
        
        
class cattleform(forms.ModelForm):
    class Meta:
        model = models.cattler
        fields = '__all__'
        
        
class sellerresetform(forms.ModelForm):
    class Meta:
        model = models.seller
        fields = ['password']
        
        
class buyerresetform(forms.ModelForm):
    class Meta:
        model = models.buyer
        fields = ['password']
        
        
