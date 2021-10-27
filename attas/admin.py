from django.contrib import admin
from .models import *


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('date', 'owner')
    search_fields = ('name', 'date')
    ordering = ('date',)
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('owner',)
    date_hierarchy = 'date'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'purchase', 'paid', 'type', 'done')
    list_filter = ('container', 'type', 'done')
    search_fields = ('name', )
    ordering = ('name', 'done')
