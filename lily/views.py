from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    register_form = None  # Initialize register_form to avoid UnboundLocalError
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Passwords do not match")
        else:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, "Registration successful!")
                return redirect('login')  # Redirect to login page
            else:
                messages.error(request, "Password should contain special symbols(/;,&$)")
                for field, errors in register_form.errors.items():
                    for error in errors:
                        print(f"Error in {field}: {error}")  # Print form errors to the console for debugging
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(username=User.objects.get(email=email).username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('calander')  # Redirect to home page upon successful login
            else:
                messages.error(request, "Invalid credentials")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def calander(request):
    return render(request, 'calander.html')
def tables(request):
    return render(request,'tables.html')
def tables2(request):
    return render(request,'tables2.html')
def tables4(request):
    return render(request,'tables4.html')
def tables3(request):
    return render(request,'tables3.html')
# Define festival detail views
def christmas(request):
    return render(request, 'festivals/christmas.html')
def newyear(request):
    return render(request, 'festivals/jan/newyear.html')
def guru(request):
    return render(request,'festivals/jan/guru.html')
def bhogi(request):
    return render(request,'festivals/jan/bhogi.html')
def sankranti(request):
    return render(request,'festivals/jan/sankranti.html')
def kanuma(request):
    return render(request,'festivals/jan/kanuma.html')
def swami(request):
    return render(request,'festivals/jan/swami.html')
def bosee(request):
    return render(request,'festivals/jan/bosee.html')
def republic(request):
    return render(request,'festivals/jan/republic.html')
def valentine(request):
    return render(request,'festivals/feb/valentine.html')
def shivaji(request):
    return render(request,'festivals/feb/shivaji.html')
def shiva(request):
    return render(request,'festivals/feb/shiva.html')
def holi(request):
    return render(request,'festivals/march/holi.html')
def ugadi(request):
    return render(request,'festivals/march/ugadi.html')
def ramzan(request):
    return render(request,'festivals/march/ramzan.html')
def ram(request):
    return render(request,'festivals/april/ram.html')
def mahavir(request):
    return render(request,'festivals/april/mahavir.html')
def ambedkar(request):
    return render(request,'festivals/april/ambedkar.html')
def gfriday(request):
    return render(request,'festivals/april/gfriday.html')
def easter(request):
    return render(request,'festivals/april/easter.html')
def tagore(request):
    return render(request,'festivals/may/tagore.html')
def mother(request):
    return render(request,'festivals/may/mother.html')
def buddha(request):
    return render(request,'festivals/may/buddha.html')
def bakrid(request):
    return render(request,'festivals/bakrid.html')

