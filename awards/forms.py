from django import forms
from .models import Profile,NewsLetterRecipients,Project,Review
class UploadProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_image','bio','contact','projects','username']

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =['title','image','description','link','editor']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=('review',)
