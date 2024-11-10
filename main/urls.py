from django.urls import path
from . import views
from .views import OpenPDFView

urlpatterns = [
    path('', views.main, name='main'),
    path('company/<int:id>/', views.company, name='company'),
    path('employee', views.employee, name='employee'),
    
    
    path('AddEmployee', views.AddEmployee, name='AddEmployee'),
    
    path('iqama/<int:id>/', views.iqama, name='iqama'),
    path('<int:id>/contract/', views.contract, name='contract'),
    path('<int:id>/payroll/', views.payroll, name='payroll'),
    path('<int:id>/tasks/', views.tasks, name='tasks'),
    path('<int:id>/fleet/', views.fleet, name='fleet'),
    
    path('<int:id>/others/', views.AddEmployee, name='AddEmployee'),
    
    path('<int:c>/iqama/<int:e>/', views.employeeiqama, name='employeeiqama'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('open-pdf/', OpenPDFView.as_view(), name='open_pdf'),
    path('prods', views.prods, name='prods'),
]
