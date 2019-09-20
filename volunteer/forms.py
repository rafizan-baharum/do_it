from django import forms

class PlayForm(forms.Form):
    sentiment = forms.CharField()
