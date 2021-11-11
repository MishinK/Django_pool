from django import forms

class StrForm(forms.Form):
    your_note = forms.CharField()