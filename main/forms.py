from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder' : 'Your Name',
                'class'       : 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder' : 'Your Email',
                'class'       : 'form-input',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder' : 'Subject',
                'class'       : 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder' : 'Your Message',
                'class'       : 'form-input',
                'rows'        : 5,
            }),
        }