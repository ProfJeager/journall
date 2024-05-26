from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Articles

def index(request):
    articles = Articles.objects.all()
    return render(request, 'main/index.html', {'articles': articles})


from django.shortcuts import render
from .models import Articles, UploadFile
from django.http import HttpResponse, Http404
from django.conf import settings
import os
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse

from django.http import FileResponse
from urllib.parse import quote

def view_certificate(request, certificate_filename):
    file_path = '/media/certificates/' + certificate_filename
    with open(file_path, 'rb') as file:
        response = FileResponse(file)
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = f'inline; filename="{quote(certificate_filename)}"'
    return response



def download_pdf(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

            # Set the Content-Length header to the size of the file
            response['Content-Length'] = os.path.getsize(file_path)

            return response
    else:
        raise Http404("File not found")

def display_file(request, file_name):

    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    return response

from urllib.parse import unquote

def display_pdf(request, pdf_filename):
    try:
        # Decode the URL-encoded filename
        pdf_filename = unquote(pdf_filename)

        pdf_file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', pdf_filename)

        # Check if the file exists
        if os.path.exists(pdf_file_path):
            with open(pdf_file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')

            response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
            return response
        else:
            return HttpResponse("File not found", status=404)
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error in display_pdf: {str(e)}")
        return HttpResponse("Internal Server Error", status=500)

def get_pdf_url(request, pdf_filename):
    pdf_url = reverse('news:display_pdf', kwargs={'pdf_filename': pdf_filename})
    return JsonResponse({'pdf_url': pdf_url})