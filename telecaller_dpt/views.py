from django.shortcuts import render

# Create your views here.

def telecaller_home(request):
    return render(request, 'telecaller_dpt/dashboard.html')