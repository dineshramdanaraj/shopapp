from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['address', 'ph_no']
    

class AddReviewForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    
   