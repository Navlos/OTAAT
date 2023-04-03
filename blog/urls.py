
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='home'),
    path('post/<str:pk>' ,  views.post, name ='post')
]
