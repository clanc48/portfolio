from django.urls import path
from .views import render_page
urlpatterns = [
    path('', render_page('home.html'), name='home'),
    path('projects/', render_page('projects.html'), name='projects'),
    path('services/', render_page('services.html'), name='services'),
    path('process/', render_page('process.html'), name='process'),
    path('contact/', render_page('contact.html'), name='contact'),
]
