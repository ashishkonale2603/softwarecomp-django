from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    
    path("", views.index, name='home'),
    path("services", views.services, name='services'),
    path("product", views.product, name='product'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about')

]
