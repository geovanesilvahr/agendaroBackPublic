from django.contrib import admin
from django.urls import include, path
from .views import RegisterView, UserProfileView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('business/', include('business.urls')),
    path('client/', include('client.urls')),
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='auth-login'),
    path('auth/profile/', UserProfileView.as_view(), name='auth-profile'),
]
