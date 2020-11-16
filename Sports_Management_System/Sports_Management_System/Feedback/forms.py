from django import forms
 
from .models import feedback
 
 
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        exclude = []