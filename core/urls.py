from django.urls import path

from . import views

# NOTE: no route for "" here on purpose. "/" belongs to projects.urls
# (project_list) - a second "" route here would shadow it and its redirect
# would loop forever, because project_list also lives at "/".
urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
