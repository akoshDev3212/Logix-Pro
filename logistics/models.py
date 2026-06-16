from django.db import models

# 1. Mijozlar modeli
class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Mijoz ismi")
    phone = models.CharField(max_length=50, verbose_name="Telefon")
    
    def __str__(self):
        return self.name

# 2. Haydovchilar modeli
class Driver(models.Model):
    name = models.CharField(max_length=100, verbose_name="Haydovchi ismi")
    truck_number = models.CharField(max_length=20, verbose_name="Mashina raqami")
    is_available = models.BooleanField(default=True, verbose_name="Bandmi?")

    def __str__(self):
        return f"{self.name} ({self.truck_number})"

# 3. Yuklar (Shipment) modeli
from django.db import models

class Shipment(models.Model):
    # Asosiy ma'lumotlar
    client_name = models.CharField(max_length=255, verbose_name="Mijoz nomi")
    destination = models.CharField(max_length=255, verbose_name="Manzil")
    departure = models.CharField(max_length=255, verbose_name="Jo'nash joyi")
    
    # Moliya
    contract_amount = models.CharField(max_length=100, verbose_name="Dorov summasi")
    advance_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Avans $")
    expenses_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Xarajat $")
    profit_sum = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Foyda (so'm)")
    
    # Haydovchi va mashina
    truck_number = models.CharField(max_length=50, verbose_name="Mashina raqami")
    driver_contact = models.CharField(max_length=50, verbose_name="Haydovchi kontakti")
    logist_name = models.CharField(max_length=100, verbose_name="Logist ismi")
    
    # Statuslar
    status = models.CharField(max_length=50, choices=[('plan', 'Plan'), ('yolda', 'Yo\'lda'), ('yetkazildi', 'Yetkazildi')])
    date_loading = models.DateField(verbose_name="Yuklash sanasi")
    
    def __str__(self):
        return f"{self.client_name} - {self.destination}"
    


    current_latitude = models.FloatField(verbose_name="Kenglik (Latitude)", null=True, blank=True)
    current_longitude = models.FloatField(verbose_name="Uzunlik (Longitude)", null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Oxirgi yangilanish")