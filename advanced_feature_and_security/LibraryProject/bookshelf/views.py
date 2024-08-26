from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Document

# Create your views here.
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})


def create_document(request):
    if request.method == 'POST':
        # Logic to create document
        pass
    return render(request, 'create_document.html')


def edit_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        # Logic to edit document
        pass
    return render(request, 'edit_document.html', {'document': document})


def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        # Logic to delete document
        pass
    return render(request, 'delete_document.html', {'document': document})
