from django.urls import path
from .views import page, contact, projects

urlpatterns = [
    path("", page("home.html"), name="home"),
    path("projects/", projects, name="projects"),
    path("services/", page("services.html"), name="services"),
    path("process/", page("process.html"), name="process"),
    path("contact/", contact, name="contact"),
]
