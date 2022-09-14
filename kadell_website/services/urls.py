from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import services, service_details


urlpatterns = [
    path('', services, name='services'),
    path('<str:service_title>/<int:service_id>', service_details, name='services_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
