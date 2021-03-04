from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import mymodelSerializer
from .models import mymodel


# Create your views here.
class apiViewSet(viewsets.ModelViewSet):
    queryset=mymodel.objects.all().order_by('name')
    serializer_class=mymodelSerializer

def add(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        description=request.POST['description']
    updated_mymodel=mymodel(name=name,age=age,description=description)
    updated_mymodel.save()
    return JsonResponse({'sucess':True,'error':False,'msg':'Data updated sucessfully'})    
    




