from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime, timedelta

@api_view(['GET', 'POST'])
def RoomRateListCreateView(request):
    if request.method == 'GET':
        roomrates = RoomRate.objects.all()
        serializer = RoomRateSerializer(roomrates, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT',])
def RoomRateUpdateView(request, pk):
    try:
        roomrate = RoomRate.objects.get(pk=pk)
    except RoomRate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RoomRateSerializer(roomrate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def RoomRateDeleteView(request, pk):
    try:
        roomrate = RoomRate.objects.get(pk=pk)
    except RoomRate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        roomrate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def OverriddenRoomRateListCreateView(request):
    if request.method == 'GET':
        overriddenrates = OverriddenRoomRate.objects.all()
        serializer = OverriddenRoomRateSerializer(overriddenrates, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OverriddenRoomRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def OverriddenRoomRateUpdateView(request, pk):
    try:
        overriddenrate = OverriddenRoomRate.objects.get(pk=pk)
    except OverriddenRoomRate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OverriddenRoomRateSerializer(overriddenrate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def OverriddenRoomRateDeleteView(request , pk):
    try:
        overriddenrate = OverriddenRoomRate.objects.get(pk=pk)
    except OverriddenRoomRate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        overriddenrate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def DiscountListCreateView(request):
    if request.method == 'GET':
        discounts = Discount.objects.all()
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def DiscountUpdateView(request, pk):
    try:
        discount = Discount.objects.get(pk=pk)
    except Discount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DiscountSerializer(discount, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DiscountDeleteView(request, pk):
    try:
        discount = Discount.objects.get(pk=pk)
    except Discount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        discount.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def DiscountRoomRateMappingView(request):
    if request.method == 'GET':
        discount_roomrates = DiscountRoomRate.objects.all()
        serializer = DiscountRoomRateSerializer(discount_roomrates, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DiscountRoomRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def DiscountRoomRateMappingUpdateView(request, pk):
    try:
        discount_roomrate = DiscountRoomRate.objects.get(pk=pk)
    except DiscountRoomRate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        print("DATA :", request.data)
        serializer = DiscountRoomRateSerializer(discount_roomrate, data=request.data)
        print("DATA 2 :",request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        discount_roomrate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def CalculatorRatesView(request, room_id, start_date, end_date):
    try:
        room_rate = RoomRate.objects.get(room_id=room_id)
    except RoomRate.DoesNotExist:
        return Response({"error": "RoomRate not found"}, status=status.HTTP_404_NOT_FOUND)

    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    final_rates = []
    total_final_rate = 0
    current_date = start_date

    while current_date <= end_date:
        try:
            overridden_rate = OverriddenRoomRate.objects.get(room_rate=room_rate, stay_date=current_date).overridden_rate
        except OverriddenRoomRate.DoesNotExist:
            overridden_rate = room_rate.default_rate

        discounts = Discount.objects.filter(discountroomrate__room_rate=room_rate)
        highest_discount = discounts.order_by('-discount_value').first()

        if highest_discount:
            if highest_discount.discount_type == Discount.PERCENTAGE:
                discount_amount = overridden_rate * (highest_discount.discount_value / 100)
            else:
                discount_amount = highest_discount.discount_value
        else:
            discount_amount = 0

        final_rate = overridden_rate - discount_amount
        final_rate = max(final_rate, 0)

        final_rates.append({
            "date": current_date,
            "overridden_rate": overridden_rate,
            "highest_discount": highest_discount.discount_value if highest_discount else 'None',
            "final_rate": final_rate
        })
        total_final_rate+=final_rate

        current_date += timedelta(days=1)

    return Response({"final_rate":final_rates,"total_Amount":total_final_rate}, status=status.HTTP_200_OK)