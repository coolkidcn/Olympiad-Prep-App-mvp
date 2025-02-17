from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

  
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

@login_required
def addDocument(request, mindMapName):
    try:
        member = Member.objects.get(authuser=request.user)
    except Member.DoesNotExist:
        return redirect('members/myuser_dashboard')

    try:
        mindMap = Mindmap.objects.get(name=mindMapName, viewers=member)
    except Mindmap.DoesNotExist:
        return redirect('userMaps')

    available_documents = Document.objects.filter(viewers=member) 

    if request.method == 'POST':
        document_id = request.POST.get('document')

        if document_id:
            try:
                document = Document.objects.get(pk=document_id, viewers=member)  # Ensure user owns document
                if mindMap in document.Mindmaps.all():  # Check for existing association
                    error_message = "Document is already associated with this mindmap."
                    return render(request, 'map/add_document.html', {'mindMap': mindMap, 'available_documents': available_documents, 'error_message': error_message})

                mindMap.documents.add(document)  # Link the document to the mindmap
                return redirect('userMaps')  # Redirect back to maps page
            except Document.DoesNotExist:
                error_message = "Invalid document selected."
                return render(request, 'map/add_document.html', {'mindMap': mindMap, 'available_documents': available_documents, 'error_message': error_message})
        else:
            error_message = "No document selected."
            return render(request, 'map/add_document.html', {'mindMap': mindMap, 'available_documents': available_documents, 'error_message': error_message})

    return render(request, 'map/add_document.html', {'mindMap': mindMap, 'available_documents': available_documents})


@login_required
def document_detail(request, document_name):
    try:
        member = Member.objects.get(authuser=request.user)
    except Member.DoesNotExist:
        return redirect('members/myuser_dashboard')

    try:
        document = Document.objects.get(name = document_name, viewers = member )
    except Document.DoesNotExist:  
        return HttpResponse("Document not found"+ ":" + document_name )
    return render(request, 'map/document_detail.html', {'document': document, "creator": Member.objects.get(pk = document.creatorId)})

@login_required
def create_mindmap(request):
    return HttpResponse("create map")

@login_required
def mindmap_detail(request, mindMapName):
    return HttpResponse(mindMapName)