from django import forms
from .models import Profile,NewsLetterRecipients
class UploadProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_image','bio','contact','projects']

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')