from django.urls import path
app_name='hello'
from app2.views import*
urlpatterns=[ 
    path('static_filet/',static_filet,name='static_filet')
]