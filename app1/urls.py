from django.urls import path
app_name='hai'
from app1.views import*
urlpatterns=[ 
    path('static_file/',static_file,name='static_file')
]