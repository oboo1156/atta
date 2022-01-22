from django.urls import path
from . import views

app_name = 'attas'

urlpatterns = [
    path('', views.index, name='index'),
    path('container', views.container, name='container'),
    path('container/<slug:container_slug>', views.customer, name='customer'),
    path('about', views.about, name='about'),
    path('add_container', views.add_container, name='add_container'),
    path('add_customer/<slug:container_slug>', views.add_customer, name='add_customer'),
    path('edit_customer/<str:customer_name>/<int:customer_id>', views.edit_customer, name='edit_customer'),
    path('edit_container/<slug:container_slug>', views.edit_container, name='edit_container'),
    path('delete_container/<slug:container_slug>', views.delete_container, name='delete_container'),
    path('delete_customer/<str:customer_name>/<int:customer_id>', views.delete_customer, name='delete_customer'),
]

#Sometimes err all it takes is a little patience.