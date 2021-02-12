from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(max_length=11, required=True)
    address = forms.CharField(max_length=100, required=True)
