from django import forms
from .models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['original_country' , 'destination_country','no_of_days','price','image']

