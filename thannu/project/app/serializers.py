from rest_framework import serializers
from .models import Inerg

class InergSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inerg
        fields= ['OIL','GAS','BRINE']