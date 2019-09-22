from django import forms

from signup.models import Registration


class RegistrationModelForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['nric_no', 'name', 'password', 'gender', 'race', 'address1', 'address2', 'address3',
                  'city', 'state', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput()
        }
