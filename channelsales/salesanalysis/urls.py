from django.conf.urls import url
from salesanalysis.views import fetch_data

urlpatterns = [
    url(r'^', fetch_data)
]