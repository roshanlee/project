from rest_framework import serializers
from .models import mymodel

class mymodelSerializer(serializers.Serializer):
    class Meta:
        model=mymodel
        fields=('name','description','age')
