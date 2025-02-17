from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from members.models import Document, Mindmap, Member

# Create your views here.
@login_required
def userMaps(request):
    if Member.objects.filter(authuser=request.user).exists():  
        member = Member.objects.filter(authuser = request.user)[0]
        documents = Document.objects.filter(viewers = member)
        mindmaps = Mindmap.objects.filter(viewers = member)
        for mindmap in mindmaps:
            try:
                creator = Member.objects.get(pk=mindmap.creatorId)  # Get Member by ID
                mindmap.creator_username = creator.username  # Access username
            except Member.DoesNotExist:
                mindmap.creator_username = "Unknown"  # Handle if creator not found

            
        for document in documents:
            try:
                creator = Member.objects.get(pk=document.creatorId)  # Get Member by ID
                document.creator_username = creator.username  # Access username
            except Member.DoesNotExist:
                document.creator_username = "Unknown"  # Handle if creator not fou
        context = {
        'documents': documents,
        'mindmaps': mindmaps,
        'username':member.username,
        'user':request.user,
        'member':member,
        'friends': Member.objects.filter(friends = member),
        }
        return render(request, 'map/mymaps.html', context)
    else:
        member = Member.objects.create(
        username=request.user.username,
        authuser= request.user,
        )
        context = {
            'username':member.username,
            }
        return redirect('members/myuser_dashboard')
    return HttpResponse("No Response")