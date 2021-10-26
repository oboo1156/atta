from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ContainerForm
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
