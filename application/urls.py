from django.urls import path

from application.views import home_page_view

app_name = "Application"


urlpatterns = [
    path("home/", home_page_view, name="Home")
]
