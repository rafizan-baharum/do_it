from django import forms

from account.models import Withdrawal


class WithdrawalModelForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ['withdraw_date', 'amount']

        widgets = {
            'withdraw_date': forms.DateInput(attrs={'type': 'date'}),
        }
