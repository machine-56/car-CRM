from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from .models import CustomUser

# Create your views here.
def index(request):
    return render(request, 'home.html')

def login_fn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            if user.is_superuser:
                return redirect('admin_home')
            else:
                return redirect('user_home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login_fn')

    return render(request, 'accounts/login.html')

def register_fn(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        username = request.POST.get("username")
        profile_image = request.FILES.get("profile_image")

        # Check for duplicates
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return redirect('register_fn')
        if CustomUser.objects.filter(phone=phone).exists():
            messages.error(request, "This phone number is already registered.")
            return redirect('register_fn')
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken.")
            return redirect('register_fn')

        # Create user and generate random password
        password = get_random_string(length=12)
        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            username=username,
            profile_image=profile_image
        )
        user.set_password(password)
        user.save()

        # Send login credentials via email
        subject = 'Welcome to Aurelius Motors – Account Created Successfully'
        message = (
            f"Hi {first_name},\n\n"
            f"Thank you for registering with Aurelius Motors.\n"
            f"Your account has been successfully created.\n\n"
            f"Here are your login credentials:\n"
            f"Username: {username}\n"
            f"Password: {password}\n\n"
            f"You can log in and update your profile or place car orders anytime.\n\n"
            f"Best regards,\n"
            f"Aurelius Motors Team"
        )

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        messages.success(request, "Registration successful. Login credentials have been sent to your email.")
        return redirect('login_fn')
    
    return render(request, 'accounts/register.html')

def validate_field(request):
    value = request.GET.get("value", "").strip()
    field_type = request.GET.get("type", "").strip()

    if not value or field_type not in ["email", "phone", "username"]:
        return JsonResponse({"exists": False, "error": "Invalid request"})

    filter_kwargs = {field_type: value}
    exists = CustomUser.objects.filter(**filter_kwargs).exists()

    return JsonResponse({"exists": exists})