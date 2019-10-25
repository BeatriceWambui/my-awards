from django.shortcuts import render,redirect
from django.http import JsonResponse
from .email import send_welcome_email
from .models import Profile,NewsLetterRecipients,Review
from .forms import UploadProfileForm,NewsLetterForm,ProjectForm,ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from .models import Project
from .serializer import MerchSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    users= Profile.objects.all()
    user = request.user
    post = Project.objects.all()
    myform=ReviewForm()
    form = NewsLetterForm()
    return render(request,'blueprint/index.html',{'users':users,'form':form,'post':post,'myform':myform})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    form = UploadProfileForm()
    return render(request,'blueprint/profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def uploadProfile(request):
    if request.method == 'POST':
        forms = UploadProfileForm(request.POST,request.FILES)
        if forms.is_valid():
            profile_image=form.cleaned_data['profile_image']
            saveProfile  = Profile(profile_image=profile_image)
            saveProfile.save()
            return redirect('index')
    else:
        forms=UploadProfileForm()
        return render(request,'blueprint/profile.html',{'forms':forms})

@login_required(login_url='/accounts/login/')
def UploadProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            image=form.cleaned_data['image']
            description=form.cleaned_data['description']
            link=form.cleaned_data['link']
            editor=form.cleaned_data['editor']
            recipient = Project(title=title,image=image,description=description,link=link,editor=editor)
            recipient.save()
            return redirect('index')
    else:
        form=ProjectForm()
    return render(request,'blueprint/upload.html',{'form':form})


@login_required(login_url='/accounts/login/')
def mysubscribe(request):
    if request.method == 'POSUploadProjectT':
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

def review(request):
    if request.method == 'POST':
        myform=ReviewForm(request.POST)
        if myform.is_valid():
            review = myform.cleaned_data['review']
            recipient = Review(review=review)
            recipient.save()
            HttpResponseRedirect('index')
    else:
            myform = CommentForm()
    return render(request,'blueprint/index.html',{'myform':myform})


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

class ProjectList(APIView):
    def get(self,request,format=None):
        all_merch = Project.objects.all()
        serializers = MerchSerializer(all_merch,many=True)
        permission_classes=(IsAdminOrReadOnly)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers=MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class MerchDescription(APIView):
    permission_classes =(IsAdminOrReadOnly,)
    def get_merch(self,pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404
    def get(self,request,pk,format=None):
        merch=self.get_merch(pk)
        serializers=MerchSerializer(merch)
        return Response(serializers.data)
    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status.HTTP_204_NO_CONTENT)
