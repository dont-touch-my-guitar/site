from django.conf.urls import url
from django.contrib import admin
from landing import views

urlpatterns = [
    url(r'^landing/', views.landing, name='landing'),
]
