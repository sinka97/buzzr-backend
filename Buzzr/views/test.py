from django.http import HttpResponse
from django.shortcuts import render
from ..models.order import Order
from datetime import datetime as dt


def test_webpage(request):
    q = request.GET.get('q', '')
    Order(id=q, status=Order.WAIT, start_datetime=dt.now(), points=100).save()
    order = Order.objects.filter(id=q).first()  
    context = {'q_number': q, 'status': order.status}
    return render(request, 'test/index.html', context)
