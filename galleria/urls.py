from django.conf.urls import url
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.pics, name='pics'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)