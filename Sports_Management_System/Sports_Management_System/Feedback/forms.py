from django import forms 
from .models import feedback
 
 
class FeedbackForm(forms.ModelForm):
    # name = forms.CharField(max_length=200)
    # event_name = forms.CharField(max_length=200)
    # event_id = forms.IntegerField(help_text="Enter Event ID here")
    # email = forms.EmailField(max_length=200)
    # details = forms.CharField()
    # happy=forms.BooleanField()

    class Meta:
        model = feedback
        exclude = []


    # class Meta:
    #     model = feedback
    #     exclude = ['happy','date']
        
    # customer_name = forms.CharField(max_length=100,
    #                         widget=forms.TextInput(attrs={
    #                         'class':'form-control',
    #                         'placeholder':'Your Name'
    #                         }))
    # event = forms.CharField(max_length=100,
    #                         widget=forms.TextInput(attrs={
    #                         'class':'form-control',
    #                         'placeholder':'Participating Sport'
    #                         }))
    # email = forms.EmailField(
    #                         widget=forms.TextInput(attrs={
    #                         'class':'form-control',
    #                         'placeholder':'Tournament Id'
    #                         }))
    # details = forms.CharField(
    #                         widget=forms.Textarea(attrs={
    #                         'class':'form-control',
    #                         'placeholder':'Your Phone Number'
    #                         }))
    # happy = forms.BooleanField(
    #                         widget=forms.TextInput(attrs={
    #                         'class':'form-control',
    #                         'placeholder':'Happy (Yes/No)'
    #                         }))




    # class Meta:
    #     model = feedback
    #     exclude = []