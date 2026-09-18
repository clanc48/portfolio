from django.urls import path
from .views import page, services, request_service

urlpatterns = [
    path("", page("home.html"), name="home"),
    path("services/", services, name="services"),
    path("service-areas/", page("service-areas.html"), name="service-areas"),
    path("reviews/", page("reviews.html"), name="reviews"),
    path("request-service/", request_service, name="request-service"),
]
