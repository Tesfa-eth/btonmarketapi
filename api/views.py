from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import OnSaleItemsSerializer
from .models import OnSaleItems

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'ItemsOnSell': '/onsale-items/',
        'Detail View': '/onsale-items-detail/<str:pk>',
        'Create': 'onsale-create',
        'Update': '/task-update/<str:pk>',
        'Delete' : '/task-delete/<str:pk>'
    }

    #return JsonResponse("API BASE POINT", safe=False)

    return Response(api_urls)

@api_view(['GET'])
def onSellItemsList(request):
    onSellItems = OnSaleItems.objects.all()
    serializer = OnSaleItemsSerializer(onSellItems, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def onSellItemsCreate(request):
    serializer = OnSaleItemsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
