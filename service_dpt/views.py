from django.shortcuts import redirect, render
import random
import string

# Create your views here.

def service_home(request):
    return render(request, 'service_dpt/dashboard.html')

def add_service_token(request):
    if request.method == 'POST':

        customer_name = request.POST.get('customerName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        vehicle = request.POST.get('vehicle')

        general_work = request.POST.get('general_work')
        general_price = request.POST.get('general_price')

        paint_work = request.POST.get('paint_work')
        paint_price = request.POST.get('paint_price')

        body_work = request.POST.get('body_work')
        body_price = request.POST.get('body_price')

        accident_work = request.POST.get('accident_work')
        accident_price = request.POST.get('accident_price')

        electrical_work = request.POST.get('electrical_work')
        electrical_price = request.POST.get('electrical_price')

        token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        delivery_time = '7 Days'

        total_price = sum([
            int(general_price or 0),
            int(paint_price or 0),
            int(body_price or 0),
            int(accident_price or 0),
            int(electrical_price or 0)
        ])

        data = {
            'token': token,
            'customer_name': customer_name,
            'phone': phone,
            'email': email,
            'vehicle': vehicle,
            'delivery_time': delivery_time,
            'total_price': total_price,
            'works': {
                'General Work': {'work': general_work, 'price': general_price},
                'Paint Department': {'work': paint_work, 'price': paint_price},
                'Body Repairs': {'work': body_work, 'price': body_price},
                'Accident Repairs': {'work': accident_work, 'price': accident_price},
                'Electrical': {'work': electrical_work, 'price': electrical_price},
            }
        }

        request.session['token_data'] = data
        return redirect('token_view')

    return render(request, 'service_dpt/add_token.html')

def token_view(request):
    data = request.session.get('token_data')
    if not data:
        return redirect('add_service_token')
    return render(request, 'service_dpt/token_view.html', {'data': data})

def service_flow(request):
    # tokens = ServiceToken.objects.all()
    return render(request, 'service_dpt/service_flow.html')

staff_list = [
    {
        'id': 1,
        'name': 'Daniel Brooks',
        'role': 'Paint Specialist',
        'experience': '5 Years',
        'tasks_completed': 120,
        'rating': 4.5,
        'image': 'images/profile_images/image-1.png'
    },
    {
        'id': 2,
        'name': 'Mason Turner',
        'role': 'Body Repairs Expert',
        'experience': '3 Years',
        'tasks_completed': 95,
        'rating': 4.2,
        'image': 'images/profile_images/image-2.png'
    },
    {
        'id': 3,
        'name': 'Sophie Bennett',
        'role': 'Electrical Technician',
        'experience': '4 Years',
        'tasks_completed': 110,
        'rating': 4.7,
        'image': 'images/profile_images/image-3.png'
    }
]

def staff_performance(request):
    return render(request, 'service_dpt/service_staffs.html', {'staff_list': staff_list})

def staff_profile(request, staff_id):
    staff = next((s for s in staff_list if s['id'] == staff_id), None)
    if not staff:
        return redirect('staff_performance')
    return render(request, 'service_dpt/service_staff_profile.html', {'staff': staff})