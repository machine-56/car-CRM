from django.shortcuts import redirect, render
from datetime import date, timedelta, datetime
from django.contrib import messages
from django.utils.timezone import now
from user.models import ServiceCountdown
import json
import random

# Create your views here.

def finance_home(request):
    return render(request, 'finance/finance_home.html')

def staff_salary(request):
    sales_staff = ['Alice', 'Bob', 'Charlie']
    service_staff = ['David', 'Eva', 'Frank']
    return render(request, 'finance/staff_salary.html', {
        'sales_staff_json': json.dumps(sales_staff),
        'service_staff_json': json.dumps(service_staff),
    })

def staff_attendance(request):
    name = request.GET.get('staff_name')
    department = request.GET.get('department')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    records = attendance_db.get(name, [])
    if start_date and end_date:
        records = [rec for rec in records if start_date <= format_date(rec['date']) <= end_date]
    absent_records = [rec for rec in records if rec['status'] == 'Absent']

    total_days = len(records)
    present_days = sum(1 for rec in records if rec['status'] == 'Present')
    absent_days = sum(1 for rec in records if rec['status'] == 'Absent')

    return render(request, 'finance/staff_attendance.html', {
        'name': name,
        'department': department,
        'attendance_data': absent_records,
        'total_days': total_days,
        'present_days': present_days,
        'absent_days': absent_days,
    })

def vehicle_sales_page(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    today = date.today()
    data = []
    for i in range(30):
        d = today - timedelta(days=i)
        units_sold = random.randint(1, 10)
        revenue = units_sold * 500000
        data.append({
            'date': d.strftime('%Y-%m-%d'),
            'units_sold': units_sold,
            'revenue': revenue,
        })

    if start_date and end_date:
        data = [x for x in data if start_date <= x['date'] <= end_date]
    data.reverse()

    return render(request, 'finance/vehicle_sales.html', {
        'vehicle_sales_data': data,
        'start_date': start_date or '',
        'end_date': end_date or '',
    })

def spare_parts_page(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    today = date.today()
    parts_data = []
    for i in range(30):
        d = today - timedelta(days=i)
        parts_data.append({
            'date': d.strftime('%Y-%m-%d'),
            'units_sold': random.randint(5, 20),
            'revenue': random.randint(10000, 50000),
        })

    if start_date and end_date:
        parts_data = [x for x in parts_data if start_date <= x['date'] <= end_date]
    parts_data.reverse()

    return render(request, 'finance/spare_parts.html', {
        'parts_sales_data': parts_data,
        'start_date': start_date or '',
        'end_date': end_date or '',
    })


def service_history(request):
    vehicle_number = request.GET.get('vehicle_number')
    results = []
    if vehicle_number:
        results = [s for s in SERVICE_HISTORY if s['vehicle'] == vehicle_number]
        results = sorted(results, key=lambda x: x['date'], reverse=True)
    return render(request, 'finance/service_history.html', {'results': results, 'vehicle_number': vehicle_number})

def service_detail(request, token):
    service = next((s for s in SERVICE_HISTORY if s['token'] == token), None)
    if not service:
        return redirect('service_history')
    return render(request, 'finance/service_detail.html', {'service': service})

def service_payment(request, token):
    if request.method == 'POST':
        payment_mode = request.POST.get('payment_mode')
        return redirect('print_token', token=token)
    return render(request, 'finance/service_payment.html', {'token': token, 'customer': 'John Doe', 'total': 3000})

def print_token(request, token):
    now_time = datetime.now()
    return render(request, 'finance/print_token.html', {
        'token': token,
        'status': 'Paid',
        'vehicle': 'KA01AB1234',
        'customer': 'John Doe',
        'date': now_time.strftime('%Y-%m-%d'),
        'time': now_time.strftime('%H:%M:%S'),
    })

def print_bill(request, token):
    service = next((s for s in SERVICE_HISTORY if s['token'] == token), None)
    if not service:
        return redirect('service_history')
    return render(request, 'finance/print_bill.html', {'service': service})

def set_countdown(request):
    if request.method == 'POST':
        vehicle_number = request.POST.get('vehicle_number')
        days = int(request.POST.get('days', 0) or 0)
        hours = int(request.POST.get('hours', 0) or 0)
        minutes = int(request.POST.get('minutes', 0) or 0)

        if ServiceCountdown.objects.filter(vehicle_number=vehicle_number, end_time__gt=now()).exists():
            messages.error(request, f"Countdown for {vehicle_number} already exists!")
            return redirect('set_countdown')

        end_time = now() + timedelta(days=days, hours=hours, minutes=minutes)
        ServiceCountdown.objects.create(vehicle_number=vehicle_number, end_time=end_time)
        messages.success(request, f"Countdown set for {vehicle_number}!")
        return redirect('set_countdown')

    active_countdowns = ServiceCountdown.objects.filter(end_time__gt=now())
    countdowns = []
    for item in active_countdowns:
        remaining = item.end_time - now()
        total_seconds = int(remaining.total_seconds())
        days = total_seconds // (24 * 3600)
        hours = (total_seconds % (24 * 3600)) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        time_str = f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}"
        countdowns.append({'vehicle_number': item.vehicle_number, 'time_str': time_str})

    return render(request, 'finance/set_countdown.html', {'countdowns': countdowns})

def format_date(date_str):
    d, m, y = map(int, date_str.split('-'))
    return f"{y}-{m:02d}-{d:02d}"

# ------------------ FAKE DATABASE ------------------

SERVICE_HISTORY = [
    {'token': 104, 'date': '2025-05-20', 'summary': 'Full Service', 'status': 'Pending', 'is_paid': False,
     'customer': 'John Doe', 'vehicle': 'KA01AB1234', 'email': 'john@example.com', 'phone': '9876543210',
     'items': [{'desc': 'Full Service', 'amount': 5000}, {'desc': 'Coolant top-up', 'amount': 800}], 'total': 5800},
    {'token': 103, 'date': '2025-04-15', 'summary': 'AC Repair', 'status': 'Paid', 'is_paid': True,
     'customer': 'John Doe', 'vehicle': 'KA01AB1234', 'email': 'john@example.com', 'phone': '9876543210',
     'items': [{'desc': 'AC Gas refill', 'amount': 3000}, {'desc': 'Compressor check', 'amount': 2000}], 'total': 5000},
    {'token': 102, 'date': '2025-03-10', 'summary': 'Wheel Alignment', 'status': 'Paid', 'is_paid': True,
     'customer': 'John Doe', 'vehicle': 'KA01AB1234', 'email': 'john@example.com', 'phone': '9876543210',
     'items': [{'desc': 'Wheel Alignment', 'amount': 1500}, {'desc': 'Tyre rotation', 'amount': 1000}], 'total': 2500},
    {'token': 101, 'date': '2025-02-05', 'summary': 'Oil Change', 'status': 'Paid', 'is_paid': True,
     'customer': 'John Doe', 'vehicle': 'KA01AB1234', 'email': 'john@example.com', 'phone': '9876543210',
     'items': [{'desc': 'Oil change', 'amount': 1000}, {'desc': 'Brake pads', 'amount': 2000}], 'total': 3000},
]

def generate_attendance():
    staff_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']
    data = {}
    start_date = date(2025, 3, 1)
    end_date = date(2025, 5, 4)
    delta = timedelta(days=1)
    while start_date <= end_date:
        for staff in staff_list:
            if staff not in data:
                data[staff] = []
            status = 'Present' if start_date.day % 3 != 0 else 'Absent'
            reason = '-' if status == 'Present' else 'Personal Reason'
            data[staff].append({'date': start_date.strftime('%d-%m-%Y'), 'status': status, 'reason': reason})
        start_date += delta
    return data

attendance_db = generate_attendance()

spare_parts_data = [
    {'name': 'Brake Pad', 'category': 'Braking System', 'stock': 25, 'sold': 15, 'revenue': 15000},
    {'name': 'Oil Filter', 'category': 'Engine', 'stock': 40, 'sold': 25, 'revenue': 20000},
    {'name': 'Air Filter', 'category': 'Engine', 'stock': 35, 'sold': 20, 'revenue': 12000},
    {'name': 'Battery', 'category': 'Electrical', 'stock': 15, 'sold': 10, 'revenue': 50000},
    {'name': 'Headlight', 'category': 'Electrical', 'stock': 20, 'sold': 12, 'revenue': 24000},
]
