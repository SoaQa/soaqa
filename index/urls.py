from django.urls import path
from index.views import *

app_name = 'index'

urlpatterns = [
    path('<int:page>', view=index, name='index_page'),
    path('', view=index, name='index')
]