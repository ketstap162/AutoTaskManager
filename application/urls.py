from django.urls import path

from application.views import home_page_view, delete_task_view

app_name = "Application"


urlpatterns = [
    path("", home_page_view, name="Home"),
    path("<int:pk>/delete", delete_task_view, name="OrderDelete")
]
