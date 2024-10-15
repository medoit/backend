from django.shortcuts import render
from .models import Sub
from .utils import *

def index(request):
    return render(request, "index.html")

def view_sub_list(request):
    load_sub()
    return render(request, "index.html")

def view_snls_list(request):
    load_snls()
    return render(request, "index.html")