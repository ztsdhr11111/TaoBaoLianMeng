from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    shops = Shop.objects.all()
    return render(request, 'taobao/index.html', {'shops':shops})