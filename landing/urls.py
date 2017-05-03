from django.conf.urls import url, include
from landing import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
]
