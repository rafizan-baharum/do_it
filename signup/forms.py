from django import forms

from signup.models import Registration


class RegistrationModelForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['nric_no', 'name', 'password', 'registration', 'address1', 'address2', 'address3',
                  'gender', 'race', 'city', 'state', 'birth_date']
