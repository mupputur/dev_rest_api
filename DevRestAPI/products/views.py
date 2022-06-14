from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.


def product(request, *args, **kwargs):
	# Receiving the data from the client - body , headers , params 
	body = request.body
	data = {}
	print(body)
	try:
		data = json.loads(body)
	except:
		pass
	#return JsonResponse({"message": "Success"}
	#return JsonResponse(data)
	data['headers'] = dict(request.headers)
	data['content_type'] = request.content_type
	data['params'] = dict(request.GET)
	return JsonResponse(data)


