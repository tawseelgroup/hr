from django import forms
from .models import Saudi, Nationality, Company


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-200 rounded focus:outline focus:outline-gray-200'}))
    nationality = forms.ModelChoiceField(queryset=Nationality.objects.all(), widget=forms.Select(attrs={'class': 'border border-gray-200 rounded focus:outline focus:outline-gray-200'}))
    company = forms.ModelChoiceField(queryset=Company.objects.all(), widget=forms.Select(attrs={'class': 'border border-gray-200 rounded focus:outline focus:outline-gray-200'}))
    job = forms.ChoiceField(choices=Saudi.JOB, widget=forms.Select(attrs={'class': ' border border-gray-200 rounded focus:outline focus:outline-gray-200'}))
    inwork = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'border border-gray-200 rounded focus:outline focus:outline-gray-200'}))
    salary = forms.DecimalField(initial=250.00, widget=forms.TextInput(attrs={'class': 'rounded border border-gray-200 bg-yellow-300 focus:outline focus:outline-gray-200', 'placeholder': 'Text goes here'}))
    identity = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'rounded border border-gray-200 focus:outline focus:outline-gray-200'}))
    bdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'rounded border border-gray-200 rounded focus:outline focus:outline-gray-200','type': 'date'}))
        
    # widgets = {
    #     name = forms.CharField({attrs())}
    # }

    