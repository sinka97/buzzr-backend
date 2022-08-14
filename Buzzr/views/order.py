from django.shortcuts import render
from ..models.order import Order,Merchant
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status as httpStatus
import json


@api_view(['POST'])
def accept_queue(request):
    order_id = request.data['orderId']
    merchant_id = request.data['merchantId']
    merchant = Merchant.objects.get(id=merchant_id)
    Order(id = order_id,merchant=merchant,start_datetime=datetime.datetime.now(),status='Waiting').save()
    return Response("Order has been accepted!", status=httpStatus.HTTP_200_OK)


@api_view(['POST'])
def change_status(request):
    try:
        order_id = request.data['orderId']
        merchant_id = request.data['merchantId']
        order_status = request.data['status']
        merchant = Merchant.objects.get(id=merchant_id)
        Order.objects.filter(id = order_id, merchant = merchant).update(status = order_status)
        return Response(f"Status of order {order_id} has been updated to {order_status} for {merchant_id}!", status=httpStatus.HTTP_200_OK)
    except Exception as e:
                return Response(f"Invalid request body {e}", status=httpStatus.HTTP_400_BAD_REQUEST)
  
    
@api_view(['POST'])
def query_status(request):
    try:
        order_id = request.data['orderId']
        merchant_id = request.data['merchantId']
        merchant = Merchant.objects.get(id=merchant_id)
        order = Order.objects.get(id=order_id,merchant=merchant)
        return Response(f"Status of order {order_id} for merchant {merchant.name} is {order.status}.", status=httpStatus.HTTP_200_OK)
    except Exception as e:
        return Response(f"Invalid request body {e}", status=httpStatus.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def get_orders_of_merchant(request):
    merchant_id = request.data['merchantId']
    merchant = Merchant.objects.get(id=merchant_id)
    try:
        orders = Order.objects.all().filter(merchant=merchant)
    except Order.DoesNotExist:
        return Response("No orders found", status=httpStatus.HTTP_404_NOT_FOUND)
    all_orders_of_merchant = []
    for order in orders:
        data = {'merchantId': order.merchant_id,
                'orderId': order.id,
                'status': order.status
                }
        all_orders_of_merchant.append(data)
    
    return Response(json.dumps(all_orders_of_merchant), status=httpStatus.HTTP_200_OK)