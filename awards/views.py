from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    users= Profile.objects.all()
    return render(request,'blueprint/index.html',{'users':users})

@login_required(login_url='/accounts/register/')
def profile(request):
    current_user=request.user
    return render(request,'blueprint/profile.html',)

def uploadProfile(request):   
    if request.method == 'POST':
        forms = UploadProfileForm(request.POST,request.FILES)
        if forms.is_valid():
            profile_image=form.cleaned_data['profile_image']
            saveProfile  = Profile(profile_image=profile_image)
            saveProfile.save()
            return redirect(index)
    else:
        forms=UploadProfileForm()
        return render(request,'blueprint/profile.html',{'forms':forms})

