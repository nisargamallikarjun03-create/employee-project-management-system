from django.shortcuts import render, get_object_or_404

from .models import Employee
from projects.models import Project


def home(request):
    total_employees = Employee.objects.count()

    active_employees = Employee.objects.filter(
        is_active=True
    ).count()

    total_projects = Project.objects.count()

    completed_projects = Project.objects.filter(
        status='Completed'
    ).count()

    context = {
        'total_employees': total_employees,
        'active_employees': active_employees,
        'total_projects': total_projects,
        'completed_projects': completed_projects,
    }

    return render(
        request,
        'home.html',
        context
    )


def employee_list(request):

    department = request.GET.get('department')

    if department:
        employees = Employee.objects.filter(
            department=department
        )
    else:
        employees = Employee.objects.all()

    departments = Employee.objects.values_list(
        'department',
        flat=True
    ).distinct()

    context = {
        'employees': employees,
        'departments': departments,
        'selected_department': department,
    }

    return render(
        request,
        'employees/employee_list.html',
        context
    )


def employee_detail(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    return render(
        request,
        'employees/employee_detail.html',
        {
            'employee': employee
        }
    )