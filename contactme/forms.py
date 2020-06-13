from django import forms
from contactme.models import contactdetails

class formcontactdetails(forms.ModelForm):
    class Meta:
        model=contactdetails
        fields=["sendername","email","subject","message"]