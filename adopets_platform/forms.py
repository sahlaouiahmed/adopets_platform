from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, AdoptionRequest

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PetSearchForm(forms.Form):
    species = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    breed = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))  
    country = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    posted_by = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AdoptionRequestFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

