from django.shortcuts import render
from .forms import EmployeeForm
from datetime import datetime

def check_eligibility(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            joining_date = form.cleaned_data['date_of_joining']
            experience_years = (datetime.now().date() - joining_date).days // 365
            eligible = "YES" if experience_years > 5 else "NO"
            return render(request, 'result.html', {'eligible': eligible})
    else:
        form = EmployeeForm()
    return render(request, 'form.html', {'form': form})