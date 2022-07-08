from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

#Validations
def clean_esal(self):
    inputsal = self.cleaned_data['esal']
    if inputsal < 5000:
        raise forms.ValidationError('the minimum salary should be 5000')

    return inputsal
