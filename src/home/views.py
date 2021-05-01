from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, resolve_url
from django.template import loader
from home.forms import CustomerForm
from home.models import Customer


def index(request):
    template = loader.get_template('index.html')
    context = {'message': 'Hello Django template!'}

    return HttpResponse(template.render(context, request))


def list_customers(request):
    list = Customer.objects.all()

    context = {'customersList': list}
    return render(request, 'customers.html', context)


def delete_customer(request, customerId):
    customer_for_delete = Customer.objects.get(id=customerId)
    if customer_for_delete is None:
        raise Exception(f'Customer with id {customerId} not found')
    customer_for_delete.delete()
    return redirect('customers_list_url')


def create_customer_form(request):
    context = {'url': resolve_url('create_customer'), 'form': CustomerForm(), 'button_message': 'Create'}
    return render(request, 'forms/customer.html', context)


def create_customer(request):
    if request.method != 'POST':
        raise Exception('Not POST method')

    customer_form = CustomerForm(request.POST)
    if not customer_form.is_valid():
        raise Exception('Invalid customer creation form')

    customer_form.save()
    return redirect('customers_list_url')


def find(request, customer_id):
    if customer_id is None:
        raise Exception('Need customer id')

    customer = Customer.objects.get(id=customer_id)
    if customer is None:
        raise Http404(f'Customer "{customer_id}" not found')

    context = {'customer': customer}
    return render(request, 'customer.html', context)


def update(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if customer is None:
        raise Http404(f'Customer "{customer_id}" not found')

    if request.method == 'GET':
        form = CustomerForm(instance=customer)
        context = {'url': resolve_url('update_customer', customer_id=customer.id), 'form': form, 'button_message': 'Update'}
        return render(request, 'forms/customer.html', context)
    elif request.method == 'POST':
        pass
    else:
        raise Exception('Method not allowed')