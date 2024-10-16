from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, AdoptionRequest
from .models import Pet

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


from django import forms
from .models import AdoptionRequest

class AdoptionRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        requester_name = kwargs.pop('requester_name', 'Your Name')
        owner_name = kwargs.pop('owner_name', 'Owner\'s Name')
        pet_name = kwargs.pop('pet_name', 'Pet\'s Name')
        super(AdoptionRequestForm, self).__init__(*args, **kwargs)
        self.fields['message'].initial = f"""Dear {owner_name},

I hope this message finds you well. My name is {requester_name}, and I recently came across your post about {pet_name}. I wanted to express my heartfelt interest in adopting {pet_name} and providing them with a loving home.

From the description and photos, I can tell that {pet_name} is a wonderful pet. I am particularly drawn to their [mention specific traits or behavior you admire]. I believe {pet_name} would make a perfect addition to my family. We have [mention any other pets or family members] who are equally excited about the possibility of welcoming {pet_name} into our home.

I have experience caring for [mention any relevant experience with pets], and I am fully prepared to meet {pet_name}'s needs, ensuring they live a happy and healthy life. I would love the opportunity to learn more about {pet_name} and discuss the adoption process in more detail.

Please let me know if there are any additional steps I need to take or if you require any further information from my end. You can reach me at {kwargs['initial']['email']}.

Thank you so much for considering my request. I look forward to hearing from you soon.

Best regards,
{requester_name}
"""

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



class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'breed', 'species','gender', 'description', 'photo', 'city', 'country']


