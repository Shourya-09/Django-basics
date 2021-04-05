from django.urls import path, include
from . import views

app_name = 'app12'
urlpatterns = [
    path('index/', views.index,  name='index'),
    path('other/',  views.other,  name='other'),
    path('relative/',  views.relative,  name='relative')
]
