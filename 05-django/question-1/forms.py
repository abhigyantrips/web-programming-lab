from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    address = forms.CharField(widget=forms.Textarea)
    contact_number = forms.CharField(max_length=15)
    email_id = forms.EmailField()
    english_marks = forms.IntegerField()
    physics_marks = forms.IntegerField()
    chemistry_marks = forms.IntegerField()
