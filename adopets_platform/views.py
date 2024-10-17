from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Pet ,AdoptionRequest
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, PetSearchForm, AdoptionRequestForm, AdoptionRequestFilterForm, PetForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages


# Create your views here.
class PetList(generic.ListView):
    queryset = Pet.objects.all()
    template_name = "adopets_platform/index.html"
    paginate_by = 6

        
def index(request):
    form = PetSearchForm(request.GET)
    pets = Pet.objects.all()
    if form.is_valid():
        if form.cleaned_data['species']:
            pets = pets.filter(species__icontains=form.cleaned_data['species'])
        if form.cleaned_data['breed']:
            pets = pets.filter(breed__icontains=form.cleaned_data['breed'])
        if form.cleaned_data['city']:
            pets = pets.filter(city__icontains=form.cleaned_data['city'])  
        if form.cleaned_data['country']:
            pets = pets.filter(country__icontains=form.cleaned_data['country'])  
        if form.cleaned_data['posted_by']:
            pets = pets.filter(posted_by__username__icontains=form.cleaned_data['posted_by'])
    return render(request, 'adopets_platform/index.html', {'form': form, 'pets': pets})


def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'adopets_platform/pet_detail.html', {'pet': pet})


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def adopt_request(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.pet = pet
            adoption_request.requester = request.user
            adoption_request.save()
            messages.success(request, 'Your adoption request was submitted successfully and is waiting to be approved.')
            return redirect('home') 
    else:
        form = AdoptionRequestForm()
    return render(request, 'adopets_platform/adopt_request.html', {'form': form, 'pet': pet})


@login_required
def my_adoption_requests(request):
    adoption_requests = AdoptionRequest.objects.filter(requester=request.user)
    
    if request.method == 'GET':
        form = AdoptionRequestFilterForm(request.GET)
        if form.is_valid():
            status = form.cleaned_data.get('status')
            if status:
                adoption_requests = adoption_requests.filter(status=status)
    else:
        form = AdoptionRequestFilterForm()
    
    return render(request, 'adopets_platform/adoptionrequests.html', {'adoption_requests': adoption_requests, 'form': form})


@login_required
def received_adoption_requests(request):
    pets = Pet.objects.filter(posted_by=request.user)
    adoption_requests = AdoptionRequest.objects.filter(pet__in=pets).order_by('-created_at')
    return render(request, 'adopets_platform/received_adoption_requests.html', {'adoption_requests': adoption_requests})


@require_POST
def update_status(request, request_id):
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id)
    new_status = request.POST.get('status')
    if new_status in ['pending', 'approved', 'rejected']:
        adoption_request.status = new_status
        adoption_request.save()
        messages.success(request, f'Status updated to {new_status}.')
    else:
        messages.error(request, 'Invalid status update.')
    return redirect('received_adoption_requests') 


def my_posted_pets(request):
    if request.user.is_authenticated:
        posted_pets = Pet.objects.filter(posted_by=request.user)
        return render(request, 'adopets_platform/my_posted_pets.html', {'posted_pets': posted_pets})
    else:
        return redirect('account_login')

def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.posted_by = request.user
            pet.save()
            return redirect('home')
    else:
        form = PetForm()
    return render(request, 'adopets_platform/add_pet.html', {'form': form})


@require_POST
def delete_adoption_request(request, request_id):
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id, requester=request.user)
    adoption_request.delete()
    messages.success(request, 'Adoption request successfully deleted.')
    return redirect('my_adoption_requests')
