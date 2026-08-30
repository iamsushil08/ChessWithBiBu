from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact, Gallery


def home(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save contact message
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message,
        )

        # Send email notification
        try:
            send_mail(
                subject=f"New Contact Form Submission from {first_name} {last_name}",
                message=f"""
New Contact Form Submission

Name: {first_name} {last_name}
Email: {email}

Message:
{message}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["chesswithbibu@gmail.com"],
                fail_silently=False,
            )

            messages.success(request, "Message sent successfully!")

        except Exception as e:
            import traceback
            print("========== EMAIL ERROR ==========")
            print("Email Error:", repr(e))
            traceback.print_exc()
            print("=================================")

            messages.warning(
                request,
                f"Email error: {e}",
            )
        
        return redirect("home")

    return render(request, "products/home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username:
            messages.error(request, "Username is required.")
            return redirect("login")

        if not password:
            messages.error(request, "Password is required.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")

        messages.error(request, "Invalid username or password.")

    return render(request, "products/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def gallery(request):
    images = Gallery.objects.all()
    return render(request, "products/gallery.html", {"images": images})


def donate(request):
    return render(request, "products/donation.html")