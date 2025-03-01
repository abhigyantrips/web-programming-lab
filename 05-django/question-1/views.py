from django.shortcuts import render
from .forms import StudentForm

def student_view(request):
    total_percentage = 0
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            english = form.cleaned_data['english_marks']
            physics = form.cleaned_data['physics_marks']
            chemistry = form.cleaned_data['chemistry_marks']
            total_marks = english + physics + chemistry
            total_percentage = (total_marks / 300) * 100
    else:
        form = StudentForm()
    return render(request, 'form.html', {'form': form, 'total_percentage': total_percentage})
