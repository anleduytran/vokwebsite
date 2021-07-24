from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def song(request):
    return render(request, 'song.html')