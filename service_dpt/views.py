from django.shortcuts import render
import random
import string

# Create your views here.

def service_home(request):
    return render(request, 'service_dpt/dashboard.html')

def add_service_token(request):
    token = None
    if request.method == 'POST':
        pass
        # token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return render(request, 'service_dpt/add_token.html')


def service_flow(request):
    # tokens = ServiceToken.objects.all()
    return render(request, 'service_dpt/service_flow.html')