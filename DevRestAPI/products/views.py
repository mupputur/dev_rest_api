from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from . models import ProductModel
from django.forms.models import model_to_dict
# Create your views here.


def product(request, *args, **kwargs):
	# Receiving the data from model
	product_model_data = ProductModel.objects.all().order_by("?").first() # random query set
	"""
	data = {}
	if product_model_data:
		data['id'] = product_model_data.id
		data['title'] = product_model_data.title
		data['category'] = product_model_data.category
		data['price'] = product_model_data.price
	"""
	# serilization model instance to python dict 
	data = {}
	if product_model_data:
		data = model_to_dict(product_model_data, fields=['id', 'title'])
	#return JsonResponse(data)
	return HttpResponse(json.dumps(data), headers={"content-type": "application/json"})
	
