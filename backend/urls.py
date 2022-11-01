from django.urls import path
from .views import StockViewSet

urlpatterns = [
    path('stocks/', StockViewSet.as_view({'get':'list'}), name='stocks'),
    path('stocks/<str:pk>/', StockViewSet.as_view({'get':'retrieve'}), name='stock')
]