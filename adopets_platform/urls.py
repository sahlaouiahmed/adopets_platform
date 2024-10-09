from . import views
from django.urls import path


urlpatterns = [
    path('', views.PetList.as_view(), name='home'),
]