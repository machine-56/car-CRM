from django.shortcuts import render

# Create your views here.
def sales_home(request):
    return render(request, 'sales_dpt/sales_home.html')


def upload_customers(request):
    return render(request, 'sales_dpt/upload_customers.html')


def stocks(request):
    return render(request, 'sales_dpt/stock.html')


def staffs(request):
    return render(request, 'sales_dpt/staffs.html')


from django.http import HttpResponseNotFound

def staff_profile(request, id):
    staff_data = {
        1: {
            'first_name': 'John',
            'last_name': 'Doe',
            'role': 'Senior Sales Executive',
            'attendance': {'status': 'Present', 'worked_days': 220, 'leaves': 10},
            'business': {'leads': 150, 'deals': 45, 'active': 12},
            'performance': [12, 19, 10, 14, 17],
        },
        2: {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'role': 'Sales Associate',
            'attendance': {'status': 'Absent', 'worked_days': 190, 'leaves': 20},
            'business': {'leads': 120, 'deals': 30, 'active': 8},
            'performance': [8, 14, 11, 10, 12],
        },
        3: {
            'first_name': 'Alex',
            'last_name': 'Johnson',
            'role': 'Sales Manager',
            'attendance': {'status': 'Present', 'worked_days': 230, 'leaves': 5},
            'business': {'leads': 200, 'deals': 70, 'active': 20},
            'performance': [15, 22, 18, 20, 25],
        }
    }

    staff = staff_data.get(id)
    if not staff:
        return HttpResponseNotFound("Staff not found")
    return render(request, 'sales_dpt/staff_profile.html', {'user': staff})
