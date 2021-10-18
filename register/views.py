from django.shortcuts import render, HttpResponseRedirect
from .forms import EmployeeRegisteration
from .models import Employee
# Create your views here.

#Function used for Adding Employee
def addshowemp(request):
    if request.method == 'POST':
        emp = EmployeeRegisteration(request.POST)
        if emp.is_valid():
            en = emp.cleaned_data['empno']
            nm = emp.cleaned_data['name']
            em = emp.cleaned_data['email']
            ad = emp.cleaned_data['add']
            regemp = Employee(empno=en, name=nm, email=em, add=ad)
            regemp.save()
            emp = EmployeeRegisteration()
    else:
        emp = EmployeeRegisteration()
    empdet = Employee.objects.all()
    return render(request, 'register/addshow.html', {'form': emp, 'emp':empdet})

#Function used for Updating/Editing Employee
def updatemp(request, id):
    if request.method == 'POST':
        idx = Employee.objects.get(pk=id)
        empx = EmployeeRegisteration(request.POST, instance=idx)
        if empx.is_valid():
            empx.save()
    else:
        idx = Employee.objects.get(pk=id)
        empx = EmployeeRegisteration(instance=idx)
    return render(request, 'register/updatedata.html', {'form': empx})


#Function used for Deleting Employee

def deletemp(request, id):
    if request.method == 'POST':
        idx = Employee.objects.get(pk=id)
        idx.delete()
        return HttpResponseRedirect('/')
