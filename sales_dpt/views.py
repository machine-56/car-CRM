from django.shortcuts import redirect, render

# Create your views here.
def sales_home(request):
    return render(request, 'sales_dpt/sales_home.html')


def upload_customers(request):
    if request.method == 'POST':
        return redirect('view_customer')
    return render(request, 'sales_dpt/upload_customers.html')

def view_customer(request):
    customers_data = [
        {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone': '+91 98765 43210',
            'interested_car': 'Aurelius ArcLite XR',
            'location': 'Mumbai'
        },
        {
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com',
            'phone': '+91 91234 56789',
            'interested_car': 'Nil',
            'location': 'Delhi'
        },
        {
            'name': 'Mike Johnson',
            'email': 'mike.johnson@example.com',
            'phone': '+91 99887 76655',
            'interested_car': 'Aurelius Imperial Drive',
            'location': 'Bengaluru'
        },
        {
            'name': 'Ayesha Khan',
            'email': 'ayesha.khan@example.com',
            'phone': '+91 97654 32109',
            'interested_car': 'Aurelius Inferno Z1',
            'location': 'Chennai'
        }
    ]
    return render(request, 'sales_dpt/view_customers.html', {'customers': customers_data})

def order_list(request):
    return render(request, 'sales_dpt/order_list.html')

def stocks(request):
    return render(request, 'sales_dpt/stock.html')


def staffs(request):
    return render(request, 'sales_dpt/staffs.html')


from django.http import HttpResponseNotFound

def sales_staff_profile(request, id):
    staff_data = {
        1: {
            'first_name': 'John',
            'last_name': 'Doe',
            'role': 'Senior Sales Executive',
            'attendance': {'status': 'Present', 'worked_days': 220, 'leaves': 10},
            'business': {'leads': 150, 'deals': 45, 'active': 12},
            'performance': [12, 19, 10, 14, 17],
            'profile_image' : 'images/profile_images/image-1.png'
        },
        2: {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'role': 'Sales Associate',
            'attendance': {'status': 'Absent', 'worked_days': 190, 'leaves': 20},
            'business': {'leads': 120, 'deals': 30, 'active': 8},
            'performance': [8, 14, 11, 10, 12],
            'profile_image' : 'images/profile_images/image-2.png'
        },
        3: {
            'first_name': 'Alex',
            'last_name': 'Johnson',
            'role': 'Sales Manager',
            'attendance': {'status': 'Present', 'worked_days': 230, 'leaves': 5},
            'business': {'leads': 200, 'deals': 70, 'active': 20},
            'performance': [15, 22, 18, 20, 25],
            'profile_image' : 'images/profile_images/image-3.png'
        }
    }

    staff = staff_data.get(id)
    if not staff:
        return HttpResponseNotFound("Staff not found")
    return render(request, 'sales_dpt/staff_profile.html', {'user': staff})


def telecaller_home(request):
    return render(request, 'telecaller_dpt/dashboard.html')