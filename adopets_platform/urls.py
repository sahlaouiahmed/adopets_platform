from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('adopt_request/<int:pet_id>/', views.adopt_request, name='adopt_request'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('my_adoption_requests/', views.my_adoption_requests, name='my_adoption_requests'),
    path('received_adoption_requests/', views.received_adoption_requests, name='received_adoption_requests'),

]

