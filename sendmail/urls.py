from django.urls import path
from . import views

urlpatterns = [
    path('wlmail', views.wlmail, name="wlmail"),
]
