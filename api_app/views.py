from django.shortcuts import render
from django.http import JsonResponse
from http import HTTPStatus

# Create your views here.
def home(request):
	a = request.GET.get('name')
	if a == 'kalyani':
		b= {'name':'hello'}
		return JsonResponse(data=b,status= HTTPStatus.OK)
	else:
		b={'name':'Parameters not found'}
		return JsonResponse(data=b,status= HTTPStatus.BAD_REQUEST)
