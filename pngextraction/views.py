from django.shortcuts import render

# Create your views here.
def pngHomeView(request):
    return render(request, "pngextraction/pngHome.html")