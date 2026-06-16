from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    # Ro'yxat ko'rinishi
    list_display = (
        'client_name', 
        'destination', 
        'date_loading', 
        'truck_number', 
        'status', 
        'profit_sum'
    )
    
    # Filtrlar
    list_filter = ('status', 'date_loading', 'logist_name')
    
    # Qidiruv
    search_fields = ('client_name', 'destination', 'truck_number', 'logist_name')
    
    # Jadvalning o'zida tahrirlash
    list_editable = ('status',)
    
    # Sana bo'yicha navigatsiya
    date_hierarchy = 'date_loading'

    # Ma'lumotlarni guruhlash
    fieldsets = (
        ('Mijoz va Manzil', {
            'fields': ('client_name', 'destination', 'departure')
        }),
        ('Moliyaviy ma\'lumotlar', {
            'fields': ('contract_amount', 'advance_usd', 'expenses_usd', 'profit_sum')
        }),
        ('Transport va Logistika', {
            'fields': ('truck_number', 'driver_contact', 'logist_name', 'status', 'date_loading')
        }),
        ('GPS Kuzatuv', {
            'fields': ('current_latitude', 'current_longitude'),
            'description': "Google Maps orqali topilgan koordinatalarni kiriting."
        }),
    )