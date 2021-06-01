from django.urls import path
from .views import *

app_name = 'hlx'
urlpatterns = [
    path('addCategory', addCategory, name='addCategory')
]