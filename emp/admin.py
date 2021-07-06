from django.contrib.admin import filters
from resto.views import register
from django.contrib import admin
from .models import Emp,EmpQulification,EmpSalary,EmpWork
@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','username','age','email','phone','address','password',
   'dateofjoin','post')
    search_fields=('username','email')
    ordering=('id',)
    list_filter=('post',)

@admin.register(EmpQulification)
class EmpQulificationAdmin(admin.ModelAdmin):
    list_display=('isHighSchoolGraduate','isUndergraduate','isCollegeGraduate')
    ordering=('id',)

@admin.register(EmpWork)
class EmpWorkAdmin(admin.ModelAdmin):
    list_display=('company_name','your_post','join_company_date','leave_company_date')
    search_fields=('company_name',)
    ordering=('id',)
    
@admin.register(EmpSalary)
class EmpSalaryAdmin(admin.ModelAdmin):
    list_display=('salarydate','monthofsalary','amount')
    ordering=('id',)
    

