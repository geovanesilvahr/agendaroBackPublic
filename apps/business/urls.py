from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AgendaViewSet, 
    RegisterBusinessSet, 
    ScheduleViewSet,
    BusinessViewSet,
    get_agendas_by_business,
    get_business_id,
    get_schedules_by_business,
)

app_name = 'business'

router = DefaultRouter()
router.register(r'business', BusinessViewSet, basename='business')
router.register(r'agendas', AgendaViewSet, basename='agendas')
router.register(r'schedules', ScheduleViewSet, basename='schedule')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', RegisterBusinessSet.as_view(), name='register-business'),
    path('register/', RegisterBusinessSet.as_view(), name='register-business'),
    path('business/<int:id>/', get_business_id, name='business-all'),
    path('business/<int:business_id>/agendas/', get_agendas_by_business, name='agendas-by-business'),
    path('agenda/<int:agenda_id>/schedules/', get_schedules_by_business, name='schedules-by-agenda'),
]
