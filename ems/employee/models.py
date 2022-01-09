from django.db import models


# Create your models here.


#  To create The EmployeeModel module
#####################################################################################
## DecisionModel Table ##
# Class name  : EmployeeModel  
# Description : This EmployeeModel class is used to create a EmployeeModel Table
# Fields       : id,name, email, designation, status, created, updated
######################################################################################

class EmployeeModel(models.Model):
	id=models.AutoField(primary_key=True, unique=True)
	name=models.CharField(max_length=200)
	email= models.EmailField(max_length=200, unique=True)
	designation=models.CharField(max_length=200)
	age=models.IntegerField()
	active = True
	In_active = False
	Status_option = (
		(active, 'Active'),
		(In_active, 'In active')
	)
	status = models.BooleanField(
		max_length=10,
		choices=Status_option,
		default=active,
	)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

