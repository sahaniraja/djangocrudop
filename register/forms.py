from django import forms
from .models import Employee

class EmployeeRegisteration(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empno', 'name', 'email', 'add']
        widgets = {
            'empno': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'add': forms.Textarea(attrs={'class': 'form-control'}),
        }