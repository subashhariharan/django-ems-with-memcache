from django.urls import path
from employee import views

urlpatterns = [
    path('Employees/', views.employee_list, name='employee_list'),
    path('EmployeeDetails/', views.employee_details, name='employee_details'),
    path('AddEmployee/', views.add_employee, name='add_employee'),
    path('DeleteEmployee/', views.delete_employee, name='delete_employee'),
    path('UpdateEmployee/', views.update_employee, name='DeleteEmployee'),

]