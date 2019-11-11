from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.art, name='art'),
    path('featured/', views.featured, name='featured'),
    path('<int:id>/',views.inspect, name='inspect'), # received art id from featured and relates this to a view: inspect
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# simply used static during developmental stage to ensure media file are accessible, not used during deployment.

