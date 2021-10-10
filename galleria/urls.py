from django.conf.urls import url,include
from . import views

urlpatterns=[
url('^$/', views.pics, name='pics'),
# url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]