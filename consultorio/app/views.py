from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start(request):
    #return HttpResponse(
        #"Meu primeiro response html django")
    return render(request, 'test.html')

def login(request):
    return render(request, 'login.html')

def create_doc(request):
    return render(request, 'create_doc.html')

def read_doc(request):
    return render(request, 'read_doc.html')