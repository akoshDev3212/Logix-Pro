from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('shipment/<int:pk>/', views.shipment_detail, name='shipment_detail'),
    path('search/', views.search_shipment, name='search_shipment'), # Mana shu qator yetishmayapti
    path('export-pdf/', views.export_pdf, name='export_pdf'),
    path('update-gps/<int:shipment_id>/', views.update_gps, name='update_gps'),
]