from django.shortcuts import render, redirect
from .models import Employee
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
# Create Employee



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserSerializer

class CustomTokenRefreshView(TokenObtainPairView):
    serializer_class = UserSerializer

# Example login view using APIView
class ObtainJWTTokenView(views.APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
      

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			print(password, username, "    ::::: password, username, :::::   ")
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				print(user, "    ::::: user :::::   ")
				messages.info(request, f"You are now logged in as {username}.")
				return render(request=request, template_name="register.html", context={"register_form":form})
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

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