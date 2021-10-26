from django.urls import path
from . import views

app_name = 'attas'

urlpatterns = [
    path('', views.home, name='home'),
    path('containers/<slug:container_slug>', views.customer, name='customer'),
    path('add_container', views.add_container, name='add_container')
]

#Sometimes err all it takes is a little patience.