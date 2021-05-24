from django.shortcuts import render

# Create your views here.
def pngHomeView(request):
    if(request.method == 'POST'):
        dicom_home = request.POST['depth']
        print(dicom_home)
    return render(request, "pngextraction/pngHome.html")