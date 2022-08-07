from django.shortcuts import render
from ..models.merchant import Merchant, MerchantSchedule
import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from ..utils import postal_district_mapping
from ..serializers import MerchantSerializer

# Create your views here.
@api_view(['POST'])
def create_merchant(request):
    '''
    {'id': 1,
    'uen': '12341241',
    'name': 'merchant-name-in-kebab-case',
    'country_code': accepts integer + can leave blank,
    'phone_number': accepts integer + can leave blank,
    'unit': can leave blank,
    'block': can leave blank,
    'street': can leave blank,
    'address': 'Ntu hive Nanyang Crescent',
    'postal_code': '123123',
    'date_joined': datetime.datetime.now(),
    'type': 'UND',
    'cuisine': 'NIL',
    'operation_status': 'OPEN'}
    '''
    try:
        merchant = request.data
        district = postal_district_mapping[merchant['postal_code'][:2]]
        date_joined = datetime.datetime.now()
    except Exception as e:
        return Response(f"Error: {e}", status=status.HTTP_400_BAD_REQUEST)

    try:
        Merchant.objects.get(pk=merchant['id'])
        return Response(f"Merchant {merchant['id']} already exists!", status=status.HTTP_409_CONFLICT)
    except Merchant.DoesNotExist:
        try:
            Merchant(id=merchant['id'],uen=merchant['uen'],name=merchant["name"],address=merchant["address"],
                    postal_code=merchant["postal_code"],district=district,date_joined=date_joined,type=merchant["type"],
                    cuisine=merchant["cuisine"],operation_status=merchant["operation_status"]).save()
            return Response(f"Merchant {merchant['id']} created!", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Error: {e}", status=status.HTTP_400_BAD_REQUEST)
        