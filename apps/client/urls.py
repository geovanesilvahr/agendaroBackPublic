from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet

app_name = 'client'

router = DefaultRouter()
router.register(r'', ClientViewSet, basename='client')

urlpatterns = [
    path('api/', include(router.urls)),
]
