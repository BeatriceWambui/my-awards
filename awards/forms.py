from django import forms
from .models import Profile
class UploadProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_image','bio','contact','projects']