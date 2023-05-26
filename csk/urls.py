from django.urls import path 
from csk.views import *
csk_name='anythink'
urlpatterns=[
    path('msd/',msd,name='msd'),
]