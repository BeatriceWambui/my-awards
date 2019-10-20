from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    return render(request,'blueprint/index.html')

@login_required(login_url='/accounts/register/')
def profile(request):
    current_user=request.user
    post=Image.objects.filter(profile_id=current_user.id)
    return render(request,'blueprint/profile.html',{'post':post,'forms':form})

    