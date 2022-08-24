from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InergSerializer
from app.models import *

@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'api':'/task/',
    }
    return Response(api_urls)
@api_view(['GET'])
def tasklist(request):
    value=request.query_params.get("well")
    #print(value)
    tasks=Inerg.objects.filter(API_WELL_NUMBER=value)
    oil=0
    gas=0
    brine=0
    for i in tasks:
        oil=oil+float(i.OIL)
        print(i.OIL)
        gas=gas+float(i.GAS)
        brine=brine+float(i.BRINE)
    total_sum={
        'oil':oil,
        'gas':gas,
        'brine':brine
    }
    return Response(total_sum)
    #serializer=InergSerializer(tasks,many=True)
    #return Response(serializer.data)
