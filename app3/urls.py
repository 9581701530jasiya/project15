from django.urls import path
app_name='bye'
from app3.views import*
urlpatterns=[ 
    path('static_filett/',static_filett,name='static_filett')
]