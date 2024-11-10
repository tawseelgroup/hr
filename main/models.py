from django.db import models
# from django.http import HttpResponse
from django.urls import reverse
from django.utils.timezone import timezone
from datetime import  timedelta

# Create your models here.

class Company(models.Model):
    compname = models.CharField(max_length=30)
    tradNo = models.CharField(max_length=20)
    location = models.CharField(max_length=15)
    employees = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "companies"
    
    def __str__(self):
        return self.compname
    
    def get_absolute_url(self):
        return reverse("company", kwargs={"id": self.id}) 
    
class Nationality(models.Model):
    nationality = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "nationalities"
    
    def __str__(self):
        return self.nationality


class Contract(models.Model):
    STATUS = [
        ('ac', "active"),
        ('in', "wating"),
        ('rj', "rejected"),
        ('tr', "terminated"),
    ]
    contractNo = models.IntegerField()
    startDate = models.DateField()
    peroid = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=2, choices=STATUS)

    

class Employee(models.Model):
    JOB = [
        ('em', "administrator"),
        ('it', "IT"),
        ('en', "Engineer"),
        ('dr', "Driver"),
        ('ac', "Accountant"),
        ('wo', "Worker"),
    ]
    
    SEX = [
        ('m', "male"),
        ('f', "female"),
    ]
    name = models.CharField(max_length=100)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, default=1)
    sex = models.CharField(max_length=1, choices=SEX, default='male')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    job = models.CharField(max_length=2, choices=JOB)
    inwork = models.BooleanField(default=True)
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        verbose_name_plural = "employees"
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("employee", kwargs={"pk": self.pk})
    
    
class Saudi(Employee):
    identity = models.IntegerField()
    bdate = models.DateField()

class Iqama(models.Model):
    iqama = models.IntegerField(primary_key=True)
    issued = models.DateField()
    renewfor = models.SmallIntegerField(default=3)
    exireDate = models.DateField()
    
    def __str__(self):
        return f"{self.iqama} - {self.issued.year}"
    
    def expire(self):
        self.exireDate = self.exireDate.date + timedelta(days=self.renewfor.days)
    
class WorkLicense(models.Model):
    startfrom  = models.DateField()
    peroid = models.SmallIntegerField()

    
class NonSaudi(Employee):
    bdate = models.DateField()
    passportNo = models.CharField(max_length=20, unique=True)
    iqama = models.OneToOneField(Iqama, null=True, blank=True, on_delete=models.SET_NULL)
    workLicense = models.OneToOneField(WorkLicense, null=True, blank=True, on_delete=models.SET_NULL)
    
    
    
class Group(models.Model):
    name = models.CharField(max_length=50)
    
class Items(models.Model):
    item = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    
    
class Inventory(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
        


    
