# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
# Create your views here.

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))

def validate(request):
    user=request.user
    data=request.data
    qrcode=data['qrcode']
    print(request.data)
    try:
        profshow=Profshow.objects.get(name=request.data['name'])
    except:
        return  Response({'message':'ProfShow does not exist'})
    try:
        student=Student.objects.filter(qrcode=qrcode)
        student_serializer=StudentSerializer(student)
    except:
        return Response({'message':'Qrcode doesnt exist'})
    try:
        ticket=Tickets.objects.get(student=student)
    except:
        return Response({'message':'No more passes'})
    if ticket.number>0:
        ticket.number-=1
        ticket.save()
        return Response({'message':'Success'})
    else:
        return Response({'message':'no more passes left 2'})
        