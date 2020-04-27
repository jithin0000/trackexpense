from django import forms 

from .models import Income

class IncomeForm(forms.ModelForm):
    """ form for creating income """

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    amount =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    created_on =forms.CharField(widget=forms.TextInput(attrs={'type':'datetime-local'}))

    class Meta:
        model = Income
        fields =['name','category','amount', 'created_on']
