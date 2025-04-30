from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'service_type', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('', 'Select a service'),
                ('Family Law', 'Family Law'),
                ('Corporate Law', 'Corporate Law'),
                ('Criminal Defense', 'Criminal Defense'),
                ('Personal Injury', 'Personal Injury'),
                ('Real Estate Law', 'Real Estate Law'),
                ('Intellectual Property', 'Intellectual Property'),
            ]),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }