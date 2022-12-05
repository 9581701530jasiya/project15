from django.shortcuts import render

# Create your views here.
def static_filett(request):
    return render(request,'static_filett.html')