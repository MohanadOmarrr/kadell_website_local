from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, required=True)
    phone = forms.IntegerField(required=True)
    service = forms.CharField(max_length=250, required=True)
    date = forms.DateField(required=True)
    time = forms.TimeField(required=True)
