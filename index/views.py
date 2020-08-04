from django.shortcuts import render
from django.forms.models import model_to_dict
from django.template.defaulttags import register

# Create your views here.
from index.models import Employee


@register.filter
def get_range(employees):
    if employees % 5 == 0:
        pages_count = employees // 5
    else:
        pages_count = (employees // 5) + 1
    return [i+1 for i in range(pages_count)]


def index(request, page=None):
    hop = 5
    if page and page > 1:
        fid, lid = hop*page-hop+1, hop*page
        employees = Employee.objects.all()[fid-1:lid]
    else:
        employees = Employee.objects.all()[0:hop]
    employees_count = Employee.objects.count()
    context = {'employees': [model_to_dict(i) for i in employees], 'emp_count': employees_count}
    return render(request=request, template_name='index.html', context=context)
