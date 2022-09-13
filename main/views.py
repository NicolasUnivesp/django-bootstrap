from django.shortcuts import render
from main.forms import MainForm

# Create your views here.
def index(request):
    return render(request, 'form.html', {'form': MainForm()})