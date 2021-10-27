from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Container(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)#change to  non-nullable later
    slug = models.SlugField(max_length=200, unique_for_date='date', null=True) #change to  non-nullable later

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'containers'

    def __str__(self):
        return self.name


class Customer(models.Model):
    TYPE = (
        ('Men', 'M'),
        ('Ladies', 'L'),
        ('Children', 'C'),
        ('Youth', 'Y'),
        ('Wasawa', 'W'),
        ('Ladies&Chidren', 'L and C'),
        ('Ladies&Wasawa', 'L and W'),
        ('Ladies&Men', 'L and M'),
        ('Youth&Wasawa', 'Y and W'),
        ('Children&Wasawa', 'C and W'),
        ('Children&Youth', 'C and Y'),
    )
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    purchase = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)
    type = models.CharField(choices=TYPE, max_length=30)
    done = models.BooleanField(default=False) #make it choice to save time

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.name
