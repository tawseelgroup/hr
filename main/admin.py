from django.contrib import admin
from .models import Company, Nationality, Employee, Contract, Saudi, WorkLicense, NonSaudi, Iqama, Employee
# Register your models here.

admin.site.register(Company)
admin.site.register(Nationality)
admin.site.register(Employee)
admin.site.register(Contract)
admin.site.register(Saudi)
admin.site.register(WorkLicense)
admin.site.register(NonSaudi)
admin.site.register(Iqama)





