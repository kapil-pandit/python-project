from django.shortcuts import render, redirect
from .models import Employee
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
# Create Employee

class UserAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def insert_emp(request):
        # tk = request.headers['Token']
        # token = RefreshToken(tk)
        # token.blacklist()
        if request.method == "POST":
            EmpId = request.POST['EmpId']
            EmpName = request.POST['EmpName']
            EmpGender = request.POST['EmpGender']
            EmpEmail = request.POST['EmpEmail']
            EmpDesignation = request.POST['EmpDesignation']
            data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail, EmpDesignation= EmpDesignation)
            data.save()
    
            return redirect('show/')
        else:
            return render(request, 'insert.html')
    
    def show_emp(request):
        employees = Employee.objects.all()
        return render(request,'show.html',{'employees':employees} )

    def edit_emp(request,pk):
        employees = Employee.objects.get(id=pk)
        if request.method == 'POST':
                print(request.POST)
                employees.EmpName = request.POST['EmpName']
                employees.EmpGender = request.POST['EmpGender']
                employees.EmpEmail = request.POST['EmpEmail']
                employees.EmpDesignation = request.POST['EmpDesignation']
                employees.EmpDesignation = request.POST['EmpDesignation']
                employees.save()   
                return redirect('/show')
        context = {
            'employees': employees,
        }

        return render(request,'edit.html',context)

    def remove_emp(request, pk):
        employees = Employee.objects.get(id=pk)

        if request.method == 'POST':
            employees.delete()
            return redirect('/show')

        context = {
            'employees': employees,
        }

        return render(request, 'delete.html', context)