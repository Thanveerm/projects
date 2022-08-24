from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path('',app.views.home, name='home'),
    path('home',app.views.home, name='home'),
    path('about', app.views.about, name='about'),
    path('cont', app.views.contact, name='cont'),
    path('company', app.views.company, name='company'),
    path('work', app.views.work, name='work'),
    path('platform', app.views.platform, name='platform'),
    path('services', app.views.services, name='services'),
]