from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView)
from .views import FullDataAPIView

urlpatterns = [
    path('full-data',
         FullDataAPIView.as_view(),
         name='full-data-api'),

    path('api/schema',
         SpectacularAPIView.as_view(),
         name='schema'),

    path('api/schema/swagger-ui',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

    path('api/schema/redoc',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
]
