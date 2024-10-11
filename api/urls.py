
from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView)
from .views import InsuranceAPIView

urlpatterns = [
    path('insurance_get_data',
         InsuranceAPIView.as_view(),
         name='insurance_get_data_api'),

    path('schema',
         SpectacularAPIView.as_view(),
         name='schema'),

    path('schema/swagger-ui',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

    path('schema/redoc',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
]
