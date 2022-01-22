from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ContainerForm, CustomerForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    return render(request, 'index.html')


@login_required
def container(request):
    container_list = Container.objects.filter(owner=request.user)
    return render(request, 'container.html', {'container_list': container_list})


def about(request):
    return render(request, 'about.html')


@login_required
def customer(request, container_slug):
    container = get_object_or_404(Container, slug=container_slug)
    if container.owner != request.user:
        raise Http404
    customers = container.customer_set.all()
    return render(request, 'customer.html', {'container': container, 'customers': customers})


@login_required
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

            return redirect('attas:container')
    return render(request, 'add_container.html', {'form': form})


@login_required
def add_customer(request, container_slug):
    container = Container.objects.get(slug=container_slug)
    if container.owner != request.user:
        raise Http404
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


@login_required
def edit_customer(request, customer_name,  customer_id):
    customer = Customer.objects.get(name=customer_name, id=customer_id)
    customer_container = customer.container
    if customer_container.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = CustomerForm(instance=customer)
    else:
        form = CustomerForm(instance=customer, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('attas:customer', container_slug=customer_container.slug)
    return render(request, 'edit_customer.html', {'customer': customer, 'customer_container': customer_container,
                                                  'form': form})


@login_required
def edit_container(request, container_slug):
    container = Container.objects.get(slug=container_slug)
    if container.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = ContainerForm(instance=container)
    else:
        form = ContainerForm(instance=container, data=request.POST)
        if form.is_valid():
            edit_container = form.save(commit=False)
            edit_container.slug = slugify(container.slug)
            edit_container.owner = request.user
            edit_container.save()
            return redirect('attas:container')
    return render(request, 'edit_container.html', {'container': container, 'form': form})


@login_required
def delete_container(request, container_slug):
    container = Container.objects.get(slug=container_slug)
    if container.owner != request.user:
        raise Http404
    if request.method == 'POST':
        container.delete()
        return redirect('attas:container')
    return render(request, 'delete_container.html', {'container': container})


@login_required
def delete_customer(request, customer_name, customer_id):
    customer = Customer.objects.get(name=customer_name, id=customer_id)
    customer_container = customer.container
    if customer_container.owner != request.user:
        raise Http404
    if request.method == 'POST':
        customer.delete()
        return redirect('attas:customer', container_slug=customer_container.slug)
    return render(request, 'delete_customer.html', {'customer': customer, 'customer_container': customer_container})













