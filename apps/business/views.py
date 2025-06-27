from django.http import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Agenda, Business, Schedule
from .serializers import (AgendaSerializer, BusinessSerializer,
                          ScheduleSerializer)

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class RegisterBusinessSet(generics.CreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    lookup_field = 'id'
    
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

def get_agendas_by_business(request, business_id):
    agendas = Agenda.objects.filter(business=business_id)
    serializer = AgendaSerializer(agendas, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_schedules_by_business(request, agenda_id):
    schedules = Schedule.objects.filter(agenda=agenda_id)
    serializer = ScheduleSerializer(schedules, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_business_id(request):
    business_id = request.GET.get('business_id')
    if business_id:
        try:
            business = Business.objects.get(id=business_id)
            serializer = BusinessSerializer(business)
            return JsonResponse(serializer.data, safe=False)
        except Business.DoesNotExist:
            return JsonResponse({'error': 'Business not found'}, status=404)
    else:
        return JsonResponse({'error': 'Business ID not provided'}, status=400)