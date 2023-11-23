# transaction_app/forms.py
from django import forms
from .models import Transaction_model

class CancelTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction_model
        fields = ['name', 'description', 'is_successful']
