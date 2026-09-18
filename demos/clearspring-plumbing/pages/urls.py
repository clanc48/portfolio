from django.urls import path
from .views import render_page
urlpatterns = [
    path('', render_page('home.html'), name='home'),
    path('services/', render_page('services.html'), name='services'),
    path('service-areas/', render_page('service-areas.html'), name='service-areas'),
    path('reviews/', render_page('reviews.html'), name='reviews'),
    path('request-service/', render_page('request-service.html'), name='request-service'),
]
