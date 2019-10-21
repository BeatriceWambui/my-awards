from django.shortcuts import render
from django.http import JsonResponse
from .email import send_welcome_email
from .models import Profile,NewsLetterRecipients
from .forms import UploadProfileForm,NewsLetterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    users= Profile.objects.all()
    form = NewsLetterForm()
    return render(request,'blueprint/index.html',{'users':users,'form':form})

@login_required(login_url='/accounts/register/')
def profile(request):
    current_user=request.user
    return render(request,'blueprint/profile.html',{'form':form})

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

@login_required(login_url='/accounts/register/')
def mysubscribe(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('mysubscribe')
    else:
        form = NewsLetterForm()
    return render(request, 'blueprint/index.html',{"letterForm":form})

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

def search_results(request):

    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_project = Profile.search_by_projects(search_term)
        message = f"{search_term}"
        profiles = Profile.objects.all()

        return render(request, 'blueprint/search.html',{"message":message,"projects": searched_project})

    else:
        message = "You haven't searched for any term"
        return render(request, 'blueprint/search.html',{"message":message})