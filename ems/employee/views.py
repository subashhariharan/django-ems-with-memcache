# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from django.db.models import F
from employee.models import EmployeeModel
import json
from django.contrib.auth import authenticate, login, logout
from django.core.cache import cache



def add_employee(request):
	response_data = {}
	try:
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		emp = EmployeeModel.objects.create(**body)
		emp.save()
		cache.delete('emp_list')
		response_data['success'] = True
		response_data['message'] = "Employee Data added succesfully..!"
	except Exception as e:
		response_data['success'] = False
		response_data['message'] = '%s (%s)' % (e, type(e))
	return JsonResponse(response_data)

def employee_details(request):
	response_data = {}
	try:
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		emp_id = body['id']
		cache_key = 'emp_'+str(emp_id) # needs to be unique
		cache_time = 86400 # time in seconds for cache to be valid
		emp_data = cache.get(cache_key) # returns None if no key-value pair
		if not emp_data:
			emp_data = EmployeeModel.objects.filter(id=emp_id,status=1).values()
			if len(emp_data) :
				emp_data = emp_data[0]
				cache.set(cache_key, emp_data, cache_time)
			else:
				response_data['success'] = False
				response_data['message'] = 'No data Found'
				return JsonResponse(response_data)

		response_data['success'] = True
		response_data['data'] = emp_data
		response_data['message'] = "Employee detaills fetched..!"
		return JsonResponse(response_data)
	except Exception as e:
		response_data['success'] = False
		response_data['message'] = '%s (%s)' % (e, type(e))
		return JsonResponse(response_data)



def employee_list(request):
	response_data = {}
	try:
		cache_key = 'emp_list' # needs to be unique
		cache_time = 86400 # time in seconds for cache to be valid
		emp_data = cache.get(cache_key) 
		if not emp_data:
			emp_data = EmployeeModel.objects.filter(status=1).values()
			if len(emp_data) :
				cache.set(cache_key, emp_data, cache_time)
		response_data['success'] = True
		response_data['data'] = list(emp_data)
		response_data['message'] = "Employee List..!"
		return JsonResponse(response_data)
	except Exception as e:
		response_data['success'] = False
		response_data['message'] = '%s (%s)' % (e, type(e))
		return JsonResponse(response_data)


def update_employee(request):
	response_data = {}
	try:
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		emp_id = body['id']
		cache_key = 'emp_'+str(emp_id) 
		cache.delete(cache_key)
		cache.delete('emp_list')
		emp = EmployeeModel.objects.filter(id=body['id']).update(designation=body['designation'])
		response_data['success'] = True
		response_data['message'] = "Employee Data Updated succesfully..!"
	except Exception as e:
		response_data['success'] = False
		response_data['message'] = '%s (%s)' % (e, type(e))
	return JsonResponse(response_data)



def delete_employee(request):
	response_data = {}
	try:
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		emp_id = body['id']
		cache_key = 'emp_'+str(emp_id) 
		cache.delete(cache_key)
		cache.delete('emp_list')
		emp = EmployeeModel.objects.filter(id=emp_id).delete()
		response_data['success'] = True
		response_data['message'] = "Employee Data Deleted succesfully..!"
	except Exception as e:
		response_data['success'] = False
		response_data['message'] = '%s (%s)' % (e, type(e))
	return JsonResponse(response_data)

