from django import forms
from .models import RegistrationData

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Your Name'
                            }))
    sportname = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Participating Sport'
                            }))
    tournamentid = forms.IntegerField(
                            widget=forms.NumberInput(attrs={
                            'class':'form-control',
                            'placeholder':'Tournament Id'
                            }))
    phone = forms.CharField(max_length=10,
                            widget=forms.TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Your Phone Number'
                            }))
    email = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Your Email'
                            }))


