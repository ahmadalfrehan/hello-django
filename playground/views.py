from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from django.http import JsonResponse
import json
# Create your views here.
def htm(request):
    return render(request,'hello.html')


def sayhello(request):
    # return render(request,'hello.html')
    my_model = Person.objects.all()
    data = [{'name': model.name, 'description': model.description} for model in my_model]
    return JsonResponse(data, safe=False)


def create_my_model(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '')
        description = data.get('description', '')
        my_model = Person.objects.create(name=name, description=description)
        return JsonResponse({'id': my_model.id, 'name': my_model.name, 'description': my_model.description}, status=201)
  
    else:
        return JsonResponse({"error":'methosnotallorw'},status=405)