from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer
from django.urls import reverse_lazy

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name']

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'
    context_object_name = 'customer'

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name']

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:customer')