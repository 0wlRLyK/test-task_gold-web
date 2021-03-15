from django.urls.conf import path
from .views import MainPageView


app_name = "menu"
urlpatterns = [
    path("", MainPageView.as_view(), name="homepage")
]