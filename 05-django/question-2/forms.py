from django import forms

class EmployeeForm(forms.Form):
    employee_id = forms.ChoiceField(choices=[('1', 'Emp1'), ('2', 'Emp2')])
    date_of_joining = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))