from django.shortcuts import render

# Create your views here.
def static_file(request):
    return render(request,'static_file.html')