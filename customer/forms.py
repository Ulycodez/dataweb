from django import forms
from .models import Customer

class CourseForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']