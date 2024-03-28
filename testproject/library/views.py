from django.shortcuts import render
from . import commonresponse

# Create your views here.

def healthCheck(request):
    return commonresponse.success("Application is active",None)
