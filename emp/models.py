from django.db import models
from django.contrib.auth.models import User

class Emp(User):
    age=models.IntegerField()
    phone=models.CharField(max_length=13)
    address=models.CharField(max_length=300)
    post=models.CharField(max_length=60)
    dateofjoin=models.DateField()

class EmpQulification(models.Model):
    isHighSchoolGraduate = models.BooleanField(default=False)
    isUndergraduate = models.BooleanField(default=False)
    isCollegeGraduate = models.BooleanField(default=False)
    empq=models.OneToOneField(Emp,on_delete=models.CASCADE)

class EmpWork(models.Model):
    company_name=models.CharField(max_length=100)
    your_post=models.CharField(max_length=60)
    join_company_date=models.DateField()
    leave_company_date=models.DateField()
    empw=models.ForeignKey(Emp,on_delete=models.CASCADE)

class EmpSalary(models.Model):
    salarydate=models.DateField()
    monthofsalary=models.CharField(max_length=12)
    amount=models.IntegerField()
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)
