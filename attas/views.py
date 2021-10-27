from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ContainerForm, CustomerForm
from django.utils.text import slugify


def home(request):
    container_list = Container.objects.all()
    return render(request, 'home.html', {'container_list': container_list})


def customer(request, container_slug):
    container = get_object_or_404(Container, slug=container_slug)
    customers = container.customer_set.all()
    return render(request, 'customer.html', {'container': container, 'customers': customers})


def add_container(request):
    if request.method != 'POST':
        form = ContainerForm()
    else:
        form = ContainerForm(data=request.POST)
        if form.is_valid():
            add_container = form.save(commit=False)
            add_container.owner = request.user
            add_container.slug = slugify(add_container.name)
            add_container.save()

            return redirect('attas:home')
    return render(request, 'add_container.html', {'form': form})


def add_customer(request, container_slug):
    container = Container.objects.get(slug=container_slug)
    if request.method != 'POST':
        form = CustomerForm()
    else:
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            add_customer = form.save(commit=False)
            add_customer.container = container
            add_customer.slug = container.slug
            add_customer.save()

            return redirect('attas:customer', container_slug=container.slug)
    return render(request, 'add_customer.html', {'container': container, 'form': form})


def edit_customer(request, customer_name,  customer_id):
    customer = Customer.objects.get(name=customer_name, id=customer_id)
    customer_container = customer.container
    if request.method != 'POST':
        form = CustomerForm(instance=customer)
    else:
        form = CustomerForm(instance=customer, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('attas:customer', container_slug=customer_container.slug)
    return render(request, 'edit_customer.html', {'customer': customer, 'customer_container': customer_container,
                                                  'form': form})


def edit_container(request, container_slug):
    container = Container.objects.get(slug=container_slug)
    if request.method != 'POST':
        form = ContainerForm(instance=container)
    else:
        form = ContainerForm(instance=container, data=request.POST)
        if form.is_valid():
            edit_container = form.save(commit=False)
            edit_container.slug = slugify(container.slug)
            edit_container.owner = request.user
            edit_container.save()
            return redirect('attas:home')
    return render(request, 'edit_container.html', {'container': container, 'form': form})


def delete_container(request, container_slug):
    container = Container.objects.get(slug=container_slug)
    if request.method == 'POST':
        container.delete()
        return redirect('attas:home')
    return render(request, 'delete_container.html', {'container': container})













