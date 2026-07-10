from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from .forms import ProductForm,RegisterForm
from .models import Contact,Gallery

def home(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )

    return render(request,'products/home.html')
    
def product_list(request):
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=ProductForm()
            
    return render(request,'products/list.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegisterForm()
        
    return render(request,'products/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username= request.POST['username']
        password=request.POST['password']
        
        if not username:
            messages.error(request, "Username is required")
            return redirect('login')

        if not password:
            messages.error(request, "Password is required")
            return redirect('login')
        
        user=authenticate(request,username=username,password=password)
        
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'products/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('home')    

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if not first_name:
            messages.error(request, "First name is required.")
            return redirect('/')

        if not last_name:
            messages.error(request, "Last name is required.")
            return redirect('/')

        if not email:
            messages.error(request, "Email is required.")
            return redirect('/')

        if "@" not in email:
            messages.error(request, "Enter valid email address.")
            return redirect('/')

        if not message:
            messages.error(request, "Message cannot be empty.")
            return redirect('/')

        if len(message) < 10:
            messages.error(request, "Message must be at least 10 characters.")
            return redirect('/')

        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )

        messages.success(request, "Message sent successfully!")  
          
    return render(request, 'products/home.html')       

def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'products/gallery.html', {'images': images})   


def donate(request):
    return render(request, 'products/donation.html')         