from django import forms

from .models import Expense


class ExpenseForm(forms.ModelForm):
    """ form for create expense """


    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    amount =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    created_on =forms.CharField(widget=forms.TextInput(attrs={'type':'datetime-local'}))

    class Meta:
        model = Expense
        fields =['name', 'amount','category', 'created_on']
