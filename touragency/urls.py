from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('packages/',views.packages, name='packages'),
    path('destination/',views.destination, name='destination'),
    path('about/',views.about_us,name='about_us'),
]