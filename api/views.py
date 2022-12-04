from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import OnSaleItemsSerializer
from .models import OnSaleItems
#from .filters import OnSaleItemsFilter
from django_filters.utils import translate_validation

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'ItemsOnSell': '/onsale-items/',
        'Search Item': 'searchItem/<str:itemname>/',
        'Detail View': '/onsale-items-detail/<str:pk>',
        'Create': 'onsale-create',
        'Update': '/task-update/<str:pk>',
        'Delete' : '/task-delete/<str:pk>'
    }

    #return JsonResponse("API BASE POINT", safe=False)

    return Response(api_urls)

@api_view(['GET'])
def onSellItemsList(request):
    onSellItems_query = OnSaleItems.objects.all()
    #filterset = OnSaleItemsFilter(request.GET, queryset=onSellItems_query)
    # if filterset.is_valid():
    #     onSellItems_query = filterset.qs

    serializer = OnSaleItemsSerializer(onSellItems_query, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filterOnSellItems(request, itemname):
    onSellItems_filterquery = OnSaleItems.objects.filter(name__icontains=itemname)
    serializer = OnSaleItemsSerializer(onSellItems_filterquery, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def onSellItemsCreate(request):
    serializer = OnSaleItemsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
