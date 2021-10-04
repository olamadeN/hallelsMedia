from django.shortcuts import render, redirect
from .models import Picture
#from . import forms

# Create your views here.
def test(request):
    test = Picture.objects.all()
    return render(request, 'uploads/gallery.html', {'gallery':test})
