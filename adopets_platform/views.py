from django.shortcuts import render
from django.views import generic
from .models import Pet


# Create your views here.
class PetList(generic.ListView):
    queryset = Pet.objects.all()
    template_name = "pet_list.html"