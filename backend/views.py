from django.shortcuts import render
from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer

# Create your views here.

class StockViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing stock instances.
    """
    serializer_class = StockSerializer
    queryset = Stock.objects.all()