from django.core.paginator import Paginator, Page
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Pet, AdoptionRequest
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, PetSearchForm, AdoptionRequestForm, AdoptionRequestFilterForm, PetForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages


# Display the home page with search functionality
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

    paginator = Paginator(pets, 15)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'adopets_platform/index.html', {'form': form, 'page_obj': page_obj})


# Display the details of a specific pet
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'adopets_platform/pet_detail.html', {'pet': pet})

# Handle user registration
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

# Submit an adoption request for a pet
@login_required
def adopt_request(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    owner_name = pet.posted_by.username
    requester_name = request.user.username
    requester_email = request.user.email
    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST, initial={'email': requester_email})
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.email = requester_email  # Set email from the logged-in user
            adoption_request.user = request.user  # Associate the request with the user
            adoption_request.pet = pet
            adoption_request.requester = request.user  # Set the requester_id
            adoption_request.save()
            return redirect('success_page')
    else:
        form = AdoptionRequestForm(initial={'email': requester_email}, requester_name=requester_name, owner_name=owner_name, pet_name=pet.name)
    return render(request, 'adopets_platform/adopt_request.html', {'form': form})

def success_page(request):
    return render(request, 'adopets_platform/success_page.html')

# Display the adoption requests made by the user
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

# Display the adoption requests received by the user
@login_required
def received_adoption_requests(request):
    pets = Pet.objects.filter(posted_by=request.user)
    adoption_requests = AdoptionRequest.objects.filter(pet__in=pets).order_by('-created_at')
    return render(request, 'adopets_platform/received_adoption_requests.html', {'adoption_requests': adoption_requests})

# Update the status of an adoption request
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

# Display the pets posted by the user
def my_posted_pets(request):
    if request.user.is_authenticated:
        posted_pets = Pet.objects.filter(posted_by=request.user)
        return render(request, 'adopets_platform/my_posted_pets.html', {'posted_pets': posted_pets})
    else:
        return redirect('account_login')

# Add a new pet to the platform
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

# Delete an adoption request made by the user
@require_POST
def delete_adoption_request(request, request_id):
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id, requester=request.user)
    adoption_request.delete()
    messages.success(request, 'Adoption request successfully deleted.')
    return redirect('my_adoption_requests')


# Edit a pet
@login_required
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.user != pet.posted_by:
        return redirect('my_posted_pets')
    
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet updated successfully.')
            return redirect('my_posted_pets')
    else:
        form = PetForm(instance=pet)
    
    return render(request, 'adopets_platform/edit_pet.html', {'form': form, 'pet': pet})

# Delete a pet
@require_POST
@login_required
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, posted_by=request.user)
    pet.delete()
    messages.success(request, 'Pet deleted successfully.')
    return redirect('my_posted_pets')