from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Shipment
from reportlab.pdfgen import canvas
import json
from django.views.decorators.csrf import csrf_exempt

def dashboard(request):
    # 'created_at' o'rniga 'date_loading' ishlatamiz
    shipments = Shipment.objects.all().order_by('-date_loading')
    
    # Statistika (status qiymatlari 'plan', 'yolda', 'yetkazildi' bo'lishi kerak)
    stats = {
        'total': Shipment.objects.count(),
        'pending': Shipment.objects.filter(status='plan').count(),
        'on_way': Shipment.objects.filter(status='yolda').count(),
        'delivered': Shipment.objects.filter(status='yetkazildi').count(),
    }
    
    context = {
        'shipments': shipments,
        'stats': stats,
        'title': 'Logix Pro - Boshqaruv Paneli'
    }
    return render(request, 'dashboard.html', context)

def shipment_detail(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)
    return render(request, 'shipment_detail.html', {'shipment': shipment})

def search_shipment(request):
    query = request.GET.get('q')
    # Qidiruvni 'client_name' yoki 'destination' bo'yicha qilamiz
    if query:
        shipments = Shipment.objects.filter(client_name__icontains=query) | Shipment.objects.filter(destination__icontains=query)
    else:
        shipments = Shipment.objects.all()
    
    # Qidiruv paytida ham stats kerak bo'lsa, uni qo'shamiz
    stats = {'total': shipments.count()} 
    return render(request, 'dashboard.html', {'shipments': shipments, 'query': query, 'stats': stats})

def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="yuklar_hisoboti.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "Logix Pro - Yuklar Hisoboti")
    p.setFont("Helvetica", 10)
    
    shipments = Shipment.objects.all()
    y = 750
    for s in shipments:
        # Yangi maydon nomlarini ishlatamiz
        text = f"Mijoz: {s.client_name} | Manzil: {s.destination} | Mashina: {s.truck_number} | Status: {s.status}"
        p.drawString(50, y, text)
        y -= 20
        if y < 50: # Sahifa tugasa yangisini ochish
            p.showPage()
            p.setFont("Helvetica", 10)
            y = 800
            
    p.showPage()
    p.save()
    return response










@csrf_exempt
def update_gps(request, shipment_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        shipment = Shipment.objects.get(id=shipment_id)
        shipment.current_latitude = data['lat']
        shipment.current_longitude = data['lon']
        shipment.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)