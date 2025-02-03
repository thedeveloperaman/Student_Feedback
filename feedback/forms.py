from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['student_name', 'email', 'roll_number', 'contact_number','subject','feedback_text']
        widgets = {
            'student_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'roll_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'contact_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'feedback_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': ''
            }),
        }