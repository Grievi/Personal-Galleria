from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.pics, name='pics'),
    path('search/', views.search_results, name='search'),
    path('location/<location>/', views.image_location, name='location'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)