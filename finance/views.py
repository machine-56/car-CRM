from django.shortcuts import render
from datetime import date, timedelta

import json

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

    return render(request, 'finance/staff_attendance.html', {
        'name': name,
        'department': department,
        'attendance_data': records,
    })








def format_date(date_str):
    d, m, y = map(int, date_str.split('-'))
    return f"{y}-{m:02d}-{d:02d}"

def generate_attendance():
    # 3 staff per department
    staff_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']
    data = {}

    start_date = date(2025, 3, 1)
    end_date = date(2025, 5, 4)
    delta = timedelta(days=1)

    while start_date <= end_date:
        for staff in staff_list:
            if staff not in data:
                data[staff] = []
            # Randomly assign present/absent + reason
            status = 'Present' if start_date.day % 3 != 0 else 'Absent'
            reason = '-' if status == 'Present' else 'Personal Reason'
            data[staff].append({
                'date': start_date.strftime('%d-%m-%Y'),
                'status': status,
                'reason': reason
            })
        start_date += delta

    return data

attendance_db = generate_attendance()