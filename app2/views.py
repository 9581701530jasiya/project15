from django.shortcuts import render

# Create your views here.
def static_filet(request):
    return render(request,'static_filet.html')