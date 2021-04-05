from django.urls import path, include
from . import views

app_name = 'app12'
urlpatterns = [
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name='user_login'),
    # path('')
    # path('base/',views.base,name="base")
]
