from django.shortcuts import render
# Create your viedef index(request):
def index(request):
    return render(request, "index.html")